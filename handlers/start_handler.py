import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command"""
    logger.info(f"Received /start command from user {update.effective_user.id}")
    
    welcome_message = """Привет! 👋

Я помогу тебе придумать, что приготовить из продуктов в твоём холодильнике.

Просто отправь мне список продуктов, и я предложу рецепт!

Например: "курица, рис, морковь, лук" """
    
    await update.message.reply_text(welcome_message)
    logger.info(f"Sent welcome message to user {update.effective_user.id}")
