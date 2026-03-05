# Telegram Recipe Bot 🍽

Telegram-бот "Что приготовить из холодильника" - кулинарный помощник, который генерирует рецепты на основе доступных продуктов с использованием OpenAI API.

## Возможности

- 🤖 Команда `/start` с приветственным сообщением
- 📝 Приём списка продуктов в свободной форме
- 🍳 Генерация персонализированных рецептов через ChatGPT
- ⚡ Быстрые ответы через webhook
- 🔒 Безопасное хранение API ключей

## Технологии

- Python 3.11+
- python-telegram-bot 20.7
- OpenAI API
- Flask (webhook server)
- Railway (deployment)

## Локальная разработка

### Требования

- Python 3.11+
- Telegram Bot Token (получить у [@BotFather](https://t.me/botfather))
- OpenAI API Key

### Установка

1. Клонировать репозиторий:
```bash
git clone <repository-url>
cd telegram-recipe-bot
```

2. Создать виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

3. Установить зависимости:
```bash
pip install -r requirements.txt
```

4. Создать `.env` файл:
```bash
cp .env.example .env
```

5. Заполнить `.env` файл:
```
TELEGRAM_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
WEBHOOK_URL=https://your-domain.com/webhook
PORT=8080
```

### Запуск

```bash
python bot.py
```

## Развёртывание на Railway

### Шаг 1: Подготовка репозитория

1. Создать GitHub репозиторий
2. Запушить код:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

### Шаг 2: Настройка Railway

1. Перейти на [railway.app](https://railway.app)
2. Создать новый проект
3. Выбрать "Deploy from GitHub repo"
4. Выбрать ваш репозиторий

### Шаг 3: Настройка переменных окружения

В Railway добавить переменные:

- `TELEGRAM_TOKEN` - токен вашего Telegram бота
- `OPENAI_API_KEY` - ключ OpenAI API
- `WEBHOOK_URL` - URL вашего приложения на Railway (будет доступен после деплоя)
- `PORT` - порт (Railway автоматически предоставляет, можно не указывать)

### Шаг 4: Настройка webhook

После деплоя:

1. Получить URL приложения (например: `https://your-app.railway.app`)
2. Обновить переменную `WEBHOOK_URL` в Railway:
   ```
   WEBHOOK_URL=https://your-app.railway.app/webhook
   ```
3. Railway автоматически перезапустит приложение

### Проверка работы

1. Открыть бота в Telegram
2. Отправить `/start`
3. Отправить список продуктов, например: "курица, рис, морковь"
4. Получить рецепт!

## Структура проекта

```
telegram-recipe-bot/
├── bot.py                  # Главный файл с Flask сервером
├── config.py               # Конфигурация и переменные окружения
├── requirements.txt        # Python зависимости
├── runtime.txt            # Версия Python для Railway
├── Procfile               # Команда запуска для Railway
├── .env.example           # Шаблон переменных окружения
├── .gitignore            # Git ignore файл
├── handlers/
│   ├── __init__.py
│   ├── start_handler.py   # Обработчик команды /start
│   └── recipe_handler.py  # Обработчик сообщений с продуктами
└── services/
    ├── __init__.py
    └── openai_service.py  # Сервис для работы с OpenAI API
```

## Использование

1. Запустить бота командой `/start`
2. Отправить список продуктов в любом формате:
   - "курица, картошка, лук, сыр"
   - "курица картошка лук сыр"
   - "У меня есть курица, картошка и лук"
3. Получить рецепт с:
   - Названием блюда
   - Списком ингредиентов
   - Пошаговой инструкцией
   - Временем приготовления

## Логирование

Бот логирует:
- Запуск и инициализацию
- Входящие webhook запросы
- Успешные генерации рецептов
- Ошибки API и исключения

Уровни логирования: INFO, WARNING, ERROR

## Обработка ошибок

- Пустое сообщение → "Пожалуйста отправь список продуктов."
- Ошибка OpenAI API → "Произошла ошибка при генерации рецепта. Попробуйте ещё раз."
- Все ошибки логируются для отладки

## Лицензия

MIT
