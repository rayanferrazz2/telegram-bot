from telegram import Update
from telegram.ext import CallbackContext

def help_command(update: Update, context: CallbackContext) -> None:
    """Responde ao comando /help"""
    comandos = """
    🛠️ Comandos disponíveis:
    /start - Inicia o bot
    /help - Mostra esta lista de comandos
    /news - Últimas notícias da FURIA
    /nextgame - Próximo jogo da FURIA
    /stats - Estatísticas dos jogadores
    """
    update.message.reply_text(comandos)