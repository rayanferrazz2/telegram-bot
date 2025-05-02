import requests
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext

# Carregar Token da Hugging Face
load_dotenv()
API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-j-6B"

headers = {"Authorization": f"Bearer {API_KEY}"}

def handle_message(update: Update, context: CallbackContext) -> None:
    """Responde mensagens usando GPT-J via Hugging Face"""
    user_message = update.message.text

    # Mensagem de boas-vindas se for uma saudação
    if user_message.lower() in ["oi", "olá", "hello"]:
        update.message.reply_text("🔥 Olá, FURIOSO! Bem-vindo ao FURIA Fans Telegram Bot! Como posso te ajudar hoje?. 😃")

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": user_message})
        bot_reply = response.json()[0].get("generated_text", "⚠️ Erro ao obter resposta.")
    except Exception as e:
        bot_reply = f"⚠️ Erro ao conectar à API: {str(e)}"

    update.message.reply_text(bot_reply)
