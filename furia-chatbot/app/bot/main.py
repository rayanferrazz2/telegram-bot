import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Importar os handlers organizados
from handlers.start_handler import start
from handlers.help_handler import help_command
from handlers.news_handler import news
from handlers.game_handler import next_game
from handlers.stats_handler import stats
from handlers.conversation_handler import handle_message  # Agora usando GPT-J via Hugging Face

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Adicionar os comandos do bot
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("news", news))
    dispatcher.add_handler(CommandHandler("nextgame", next_game))
    dispatcher.add_handler(CommandHandler("stats", stats))

    # Adicionar o handler para respostas conversacionais usando GPT-J
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot rodando com integração ao GPT-J via Hugging Face...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()