import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

openai.api_key = "Ksk-TeopmXofOJW3MyQfBgXpT3BlbkFJMOa1BTodmM1tXw7SHhkH"

def start(bot, update):
    update.message.reply_text("Hai! Saya adalah bot chat yang diteruskan oleh OpenAI. Bagaimana saya bisa membantu hari ini?")

def respond(bot, update):
    message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Anda: " + message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    response = response.strip().split("\n")[-1].strip()
    update.message.reply_text("AI: " + response)

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    updater = Updater("5695753273:AAFWnDAZx9Hkco6MoYDAgaJZj9XNaa-4bm8", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, respond))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
