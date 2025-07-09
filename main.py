
import os
import telebot
from telebot.types import Message

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = int(os.environ.get("ADMIN_ID"))

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def handle_start(message: Message):
    bot.send_message(message.chat.id, "Привет! Напиши свой вопрос, и мы скоро ответим.")

@bot.message_handler(func=lambda m: True)
def handle_all_messages(message: Message):
    if message.from_user.id != ADMIN_ID:
        fwd = bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
        bot.send_message(ADMIN_ID, f"(от @{message.from_user.username or 'без username'} / ID: {message.from_user.id})")
        bot.register_next_step_handler(fwd, lambda reply: handle_reply(reply, message.chat.id))

def handle_reply(reply: Message, user_id: int):
    bot.send_message(user_id, reply.text)

bot.polling()
