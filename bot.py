import openai

openai.api_key = "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"


def respond(message):
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=message,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = response.choices[0].text
  return message


# Impor library telepot
import telepot

# Set API key Telegram Bot
bot = telepot.Bot("5695753273:AAFWnDAZx9Hkco6MoYDAgaJZj9XNaa-4bm8")


def handle(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
  if content_type == 'text':
    message = msg['text']
    if message.startswith("/ask"):
      response = respond(message[5:])
      bot.sendMessage(chat_id, response)


bot.message_loop(handle)
