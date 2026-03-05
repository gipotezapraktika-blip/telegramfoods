import logging
from telegram import Update
from telegram.ext import ContextTypes
from services.openai_service import OpenAIService

logger = logging.getLogger(__name__)


async def recipe_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle text messages with ingredients"""
    
    # Get user message
    user_message = update.message.text.strip()
    
    # Validate non-empty message
    if not user_message:
        await update.message.reply_text("Пожалуйста отправь список продуктов.")
        return
    
    # Get OpenAI service from context
    openai_service: OpenAIService = context.bot_data.get('openai_service')
    
    try:
        # Generate recipe
        recipe = await openai_service.generate_recipe(user_message)
        
        # Format response
        formatted_recipe = format_recipe(recipe)
        
        # Send recipe to user
        await update.message.reply_text(formatted_recipe)
        
        logger.info(f"Successfully generated recipe for user {update.effective_user.id}")
        
    except Exception as e:
        logger.error(f"Error generating recipe: {type(e).__name__} - {str(e)}")
        await update.message.reply_text("Произошла ошибка при генерации рецепта. Попробуйте ещё раз.")


def format_recipe(recipe: str) -> str:
    """
    Format recipe with emojis and structure
    
    Args:
        recipe: Raw recipe text from OpenAI
        
    Returns:
        Formatted recipe text
    """
    # If recipe already has proper formatting, return as is
    if "🍽" in recipe or "⏱" in recipe:
        return recipe
    
    # Otherwise, add basic formatting
    lines = recipe.strip().split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Add emoji to dish name if it's the first line
        if len(formatted_lines) == 0 and not line.startswith('🍽'):
            formatted_lines.append(f"🍽 Блюдо: {line}")
        else:
            formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)
