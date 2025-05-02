import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

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

async def main():
    # Criar a aplicação corretamente
    application = Application.builder().token(TOKEN).build()

    # Adicionar os comandos do bot
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("news", news))
    application.add_handler(CommandHandler("nextgame", next_game))
    application.add_handler(CommandHandler("stats", stats))

    # Adicionar o handler para respostas conversacionais usando GPT-J
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot rodando com integração ao GPT-J via Hugging Face...")
    await application.run_polling()

if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()  # Mantém o loop rodando corretamente

