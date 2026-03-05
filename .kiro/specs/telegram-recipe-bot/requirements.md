# Requirements Document

## Introduction

Telegram-бот "Что приготовить из холодильника" - это кулинарный помощник, который принимает от пользователя список продуктов и генерирует рецепты блюд с использованием OpenAI API. Бот развёрнут на платформе Railway и работает через webhook.

## Glossary

- **Recipe_Bot**: Telegram-бот для генерации рецептов
- **User**: Пользователь Telegram, взаимодействующий с ботом
- **OpenAI_Service**: Сервис для взаимодействия с OpenAI API
- **Ingredient_List**: Текстовый список продуктов, отправленный пользователем
- **Recipe_Response**: Форматированный ответ с рецептом блюда
- **Webhook**: Механизм получения обновлений от Telegram API
- **Railway_Platform**: Платформа для развёртывания приложения

## Requirements

### Requirement 1: Команда запуска бота

**User Story:** Как пользователь, я хочу получить приветственное сообщение с инструкцией, чтобы понять как использовать бота

#### Acceptance Criteria

1. WHEN User sends /start command, THE Recipe_Bot SHALL respond with a welcome message
2. THE Recipe_Bot SHALL include usage instructions in the welcome message
3. THE welcome message SHALL be in Russian language

### Requirement 2: Получение списка продуктов

**User Story:** Как пользователь, я хочу отправить список продуктов текстовым сообщением, чтобы получить рецепт

#### Acceptance Criteria

1. WHEN User sends a text message, THE Recipe_Bot SHALL accept it as Ingredient_List
2. IF Ingredient_List is empty, THEN THE Recipe_Bot SHALL respond with "Пожалуйста отправь список продуктов."
3. THE Recipe_Bot SHALL process text messages in any format

### Requirement 3: Генерация рецепта через OpenAI API

**User Story:** Как пользователь, я хочу получить рецепт на основе моих продуктов, чтобы приготовить блюдо

#### Acceptance Criteria

1. WHEN Recipe_Bot receives valid Ingredient_List, THE OpenAI_Service SHALL send request to OpenAI API
2. THE OpenAI_Service SHALL include system prompt: "Ты кулинарный помощник. Пользователь отправляет список продуктов. Нужно предложить блюдо, которое можно приготовить из этих продуктов. Ответ должен содержать: 1. Название блюда 2. Список ингредиентов 3. Пошаговый рецепт 4. Время приготовления. Если ингредиентов мало — предложи простое блюдо. Не добавляй экзотические ингредиенты."
3. THE OpenAI_Service SHALL include Ingredient_List as user message
4. THE OpenAI_Service SHALL use ChatGPT model for recipe generation

### Requirement 4: Форматирование ответа

**User Story:** Как пользователь, я хочу получить рецепт в читаемом формате, чтобы легко следовать инструкциям

#### Acceptance Criteria

1. WHEN OpenAI_Service returns recipe, THE Recipe_Bot SHALL format Recipe_Response with dish name prefixed by "🍽 Блюдо:"
2. THE Recipe_Response SHALL include section "Ингредиенты:" with ingredient list
3. THE Recipe_Response SHALL include section "Рецепт:" with numbered steps
4. THE Recipe_Response SHALL include cooking time prefixed by "⏱ Время приготовления:"
5. THE Recipe_Bot SHALL send Recipe_Response to User

### Requirement 5: Обработка ошибок API

**User Story:** Как пользователь, я хочу получить понятное сообщение об ошибке, чтобы знать что произошло

#### Acceptance Criteria

1. IF OpenAI_Service fails to generate recipe, THEN THE Recipe_Bot SHALL respond with "Произошла ошибка при генерации рецепта. Попробуйте ещё раз."
2. THE Recipe_Bot SHALL log error details for debugging
3. THE Recipe_Bot SHALL continue operation after error

### Requirement 6: Конфигурация через переменные окружения

**User Story:** Как разработчик, я хочу хранить секретные ключи в переменных окружения, чтобы обеспечить безопасность

#### Acceptance Criteria

1. THE Recipe_Bot SHALL read TELEGRAM_TOKEN from environment variables
2. THE OpenAI_Service SHALL read OPENAI_API_KEY from environment variables
3. IF required environment variable is missing, THEN THE Recipe_Bot SHALL fail to start with descriptive error message

### Requirement 7: Развёртывание на Railway

**User Story:** Как разработчик, я хочу развернуть бота на Railway, чтобы он работал непрерывно

#### Acceptance Criteria

1. THE Recipe_Bot SHALL be deployable on Railway_Platform
2. THE Recipe_Bot SHALL use webhook mechanism for receiving Telegram updates
3. THE Recipe_Bot SHALL include Procfile for Railway deployment configuration
4. THE Recipe_Bot SHALL include runtime.txt specifying Python 3.11+
5. THE Recipe_Bot SHALL include requirements.txt with all dependencies

### Requirement 8: Структура проекта

**User Story:** Как разработчик, я хочу иметь организованную структуру проекта, чтобы легко поддерживать код

#### Acceptance Criteria

1. THE Recipe_Bot SHALL have bot.py as main entry point
2. THE Recipe_Bot SHALL have config.py for configuration management
3. THE Recipe_Bot SHALL have openai_service.py in services directory
4. THE Recipe_Bot SHALL have start_handler.py in handlers directory
5. THE Recipe_Bot SHALL have recipe_handler.py in handlers directory
6. THE Recipe_Bot SHALL have .env file for local environment variables

### Requirement 9: Зависимости проекта

**User Story:** Как разработчик, я хочу иметь все необходимые зависимости, чтобы бот работал корректно

#### Acceptance Criteria

1. THE Recipe_Bot SHALL use python-telegram-bot library for Telegram API interaction
2. THE Recipe_Bot SHALL use openai library for OpenAI API interaction
3. THE Recipe_Bot SHALL use python-dotenv library for environment variable management
4. WHERE webhook is implemented, THE Recipe_Bot SHALL use flask or fastapi framework
5. THE requirements.txt SHALL list all required dependencies with versions
