from telegram import Update
from telegram.ext import CallbackContext

def news(update: Update, context: CallbackContext) -> None:
    """Responde ao comando /news com notícias fictícias"""
    noticias = """
    📰 Últimas notícias da FURIA:
    🔥 FURIA vence torneio internacional de CS:GO!
    🏆 KSCERATO eleito MVP da competição.
    🎮 Próximo desafio será contra NAVI.
    """
    update.message.reply_text(noticias)