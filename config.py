import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

# Load environment variables from .env file (only in development)
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
        logger.info(f"Validating configuration...")
        logger.info(f"TELEGRAM_TOKEN present: {bool(cls.TELEGRAM_TOKEN)}")
        logger.info(f"OPENAI_API_KEY present: {bool(cls.OPENAI_API_KEY)}")
        logger.info(f"WEBHOOK_URL: {cls.WEBHOOK_URL}")
        logger.info(f"PORT: {cls.PORT}")
        
        if not cls.TELEGRAM_TOKEN:
            raise ValueError("Missing required environment variable: TELEGRAM_TOKEN")
        if not cls.OPENAI_API_KEY:
            raise ValueError("Missing required environment variable: OPENAI_API_KEY")
