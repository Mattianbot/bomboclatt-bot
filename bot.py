import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

async def bomboclatt_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("bomboclatt")

def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handler per tutti i messaggi di testo (esclusi comandi)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bomboclatt_reply))

    print("Bomboclatt bot is online.")
    app.run_polling()

if __name__ == "__main__":
    main()


