
# Telegram Forward-Reply Bot

Этот бот:
1. Получает сообщения от пользователей
2. Пересылает их тебе (админу)
3. Позволяет тебе отвечать через Reply, и бот пересылает сообщение обратно

## 🔧 Как развернуть на Render.com

1. Перейди на https://render.com
2. Зарегистрируйся и создай новый Web Service
3. Подключи GitHub или выбери Deploy from ZIP
4. Укажи:
   - Start Command: `python main.py`
   - Runtime: Python 3.11+
5. Перейди во вкладку Environment → добавь переменные:
   - `BOT_TOKEN`: твой токен бота
   - `ADMIN_ID`: твой Telegram ID

Бот будет работать 24/7 без хостинга на твоём компьютере.
