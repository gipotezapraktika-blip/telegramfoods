import logging
from openai import OpenAI, OpenAIError

logger = logging.getLogger(__name__)


class OpenAIService:
    """Service for interacting with OpenAI API"""
    
    SYSTEM_PROMPT = """Ты кулинарный помощник. Пользователь отправляет список продуктов. 
Нужно предложить блюдо, которое можно приготовить из этих продуктов. 
Ответ должен содержать:
1. Название блюда
2. Список ингредиентов
3. Пошаговый рецепт
4. Время приготовления

Если ингредиентов мало — предложи простое блюдо. 
Не добавляй экзотические ингредиенты."""
    
    def __init__(self, api_key: str):
        """Initialize OpenAI client with API key"""
        self.client = OpenAI(api_key=api_key)
    
    async def generate_recipe(self, ingredients: str) -> str:
        """
        Generate recipe from ingredients list
        
        Args:
            ingredients: Text list of ingredients
            
        Returns:
            Generated recipe text
            
        Raises:
            OpenAIError: If API request fails
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.SYSTEM_PROMPT},
                    {"role": "user", "content": ingredients}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            recipe = response.choices[0].message.content
            return recipe
            
        except OpenAIError as e:
            logger.error(f"OpenAI API error: {type(e).__name__} - {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in generate_recipe: {type(e).__name__} - {str(e)}")
            raise
