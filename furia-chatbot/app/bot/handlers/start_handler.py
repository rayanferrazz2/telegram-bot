from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    """Responde ao comando /start"""
    update.message.reply_text("🔥 Vamos lá, FURIOSO! Use /help para ver os comandos disponíveis.")