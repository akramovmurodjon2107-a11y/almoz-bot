import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Логларни ёқиш
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("8712513053:AAHagpnYn2trev2CoJY7E8XOak3PL62FuD4")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Ассалому алайкум!\n\n"
        "Almoz_tj расмий ботига хуш келибсиз!\n"
        "Мен сизга ёрдам беришга тайёрман.\n\n"
        "Буюртма бериш учун /help ни босинг."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Бот командалари:\n"
        "/start - Ботни ишга тушириш\n"
        "/help - Ёрдам\n\n"
        "Саволингизни ёзинг, жавоб бераман!"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"✅ Қабул қилинди: {update.message.text}")

def main():
    if not BOT_TOKEN:
        print("XATO: BOT_TOKEN топилмади!")
        return
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("✅ Almoz bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
