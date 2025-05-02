from telegram import Update
from telegram.ext import CallbackContext

def stats(update: Update, context: CallbackContext) -> None:
    """Responde ao comando /stats com estatísticas dos jogadores"""
    update.message.reply_text("📊 Estatísticas dos jogadores:\nKSCERATO - Rating: 1.25\nyuurih - Rating: 1.20")