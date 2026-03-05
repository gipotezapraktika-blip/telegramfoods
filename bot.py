import logging
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import Config
from services.openai_service import OpenAIService
from handlers.start_handler import start_command
from handlers.recipe_handler import recipe_message

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Global bot application
bot_app = None


async def setup_bot():
    """Initialize and configure the bot application"""
    global bot_app
    
    # Validate configuration
    Config.validate()
    logger.info("Configuration validated successfully")
    
    # Create bot application
    bot_app = Application.builder().token(Config.TELEGRAM_TOKEN).build()
    
    # Initialize OpenAI service
    openai_service = OpenAIService(Config.OPENAI_API_KEY)
    bot_app.bot_data['openai_service'] = openai_service
    
    # Register handlers
    bot_app.add_handler(CommandHandler("start", start_command))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, recipe_message))
    
    logger.info("Bot handlers registered successfully")
    
    # Initialize bot
    await bot_app.initialize()
    await bot_app.start()
    
    # Set webhook
    if Config.WEBHOOK_URL:
        await bot_app.bot.set_webhook(url=Config.WEBHOOK_URL)
        logger.info(f"Webhook set to: {Config.WEBHOOK_URL}")
    
    return bot_app


@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle incoming webhook requests from Telegram"""
    try:
        # Parse update
        update_data = request.get_json(force=True)
        update = Update.de_json(update_data, bot_app.bot)
        
        # Process update
        asyncio.run(bot_app.process_update(update))
        
        logger.info(f"Processed webhook update: {update.update_id}")
        return {'ok': True}
        
    except Exception as e:
        logger.error(f"Error processing webhook: {type(e).__name__} - {str(e)}")
        return {'ok': False, 'error': str(e)}, 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return {'status': 'ok'}


def main():
    """Main entry point"""
    try:
        # Setup bot
        asyncio.run(setup_bot())
        
        # Start Flask server
        port = Config.PORT
        logger.info(f"Starting Flask server on port {port}")
        app.run(host='0.0.0.0', port=port)
        
    except Exception as e:
        logger.error(f"Failed to start bot: {type(e).__name__} - {str(e)}")
        raise


if __name__ == '__main__':
    main()
