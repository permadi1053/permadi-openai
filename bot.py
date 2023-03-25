from keep_alive import keep_alive
import openai

openai.api_key = "your API"


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
bot = telepot.Bot("your API")


def handle(msg):
  content_type, chat_type, chat_id = telepot.glance(msg)
  if content_type == 'text':
    message = msg['text']
    if message == "/start":
      bot.sendMessage(
        chat_id,
        "Halloi, gunakan format:\n" \
        "🔶 Format: '/ask perintah'\n" \
        "🔶 Contoh: '/ask apa kabar?'"
      )
    elif message.startswith("/ask"):
      response = respond(message[5:])
      bot.sendMessage(chat_id, response)


bot.message_loop(handle)

# Jalankan server agar aplikasi terus berjalan di repl.it
keep_alive()
