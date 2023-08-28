import openai
import telebot

openai.api_key = "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"

TELEGRAM_TOKEN = "6259005457:AAFblf-F10t0NaWF8-2Arr731V584tPlmlA"
bot = telebot.TeleBot(TELEGRAM_TOKEN)

what = "A sarcastic chatbot named 'Pedalov Dzi', created by Armenian scientists, who answers shortly, and usually ends sentences with 'axpers' or 'hopar'."
messages = [{"role": "system", "content": what}]

@bot.message_handler(func=lambda message: True)
def handle_message(message):

    user_message = message.text
    messages.append({"role": "user", "content": user_message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    bot_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "", "content": bot_reply})
    
    bot.send_message(message.chat.id, bot_reply)

bot.polling()
