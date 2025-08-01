from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📷 Photo mila! Thoda wait karo...")
    await update.message.reply_text("✅ Feedback: Achi photo hai, thoda brightness badhao.")
app = ApplicationBuilder().token(8310453754:AAHDLyVDO5Ku-s3nszc-6R3cr-vXU95v8uo").build()
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
app.run_polling()