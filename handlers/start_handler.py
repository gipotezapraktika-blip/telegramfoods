from telegram import Update
from telegram.ext import ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command"""
    welcome_message = """Привет! 👋

Я помогу тебе придумать, что приготовить из продуктов в твоём холодильнике.

Просто отправь мне список продуктов, и я предложу рецепт!

Например: "курица, рис, морковь, лук" """
    
    await update.message.reply_text(welcome_message)
