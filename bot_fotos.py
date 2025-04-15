from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Seu token do bot do Telegram
TOKEN = '7729985668:AAEfyBn8UOYnDsJLKpSryDF404u6nQk7XsI'

# Link da Hotmart
HOTMART_LINK = 'https://pay.hotmart.com/H99226358I'

# Mensagem personalizada
MENSAGEM = f"Hola amor, aca tenes mi fotito 💕\n\n👉 {HOTMART_LINK}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MENSAGEM)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot está rodando... ✅")
    app.run_polling()
