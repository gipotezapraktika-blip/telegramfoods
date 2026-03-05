import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for bot settings"""
    
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    WEBHOOK_URL = os.getenv('WEBHOOK_URL')
    PORT = int(os.getenv('PORT', '8080'))
    
    @classmethod
    def validate(cls):
        """Validate that required environment variables are set"""
        if not cls.TELEGRAM_TOKEN:
            raise ValueError("Missing required environment variable: TELEGRAM_TOKEN")
        if not cls.OPENAI_API_KEY:
            raise ValueError("Missing required environment variable: OPENAI_API_KEY")
