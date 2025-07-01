from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction
import time
import os

def start(update, context):
    update.message.reply_text("Scrivimi qualcosa... 😎")

def bomboclatt_reply(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    time.sleep(1.5)
    update.message.reply_text("Bomboclatt")

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, bomboclatt_reply))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
