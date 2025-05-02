from telegram import Update
from telegram.ext import CallbackContext

def next_game(update: Update, context: CallbackContext) -> None:
    """Responde ao comando /nextgame com informações do próximo jogo"""
    update.message.reply_text("🎮 Próximo jogo da FURIA: Sexta-feira, 20h contra NAVI!")