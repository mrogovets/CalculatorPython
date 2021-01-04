"""Doc."""


import telebot
from pyowm import OWM

owm = OWM('16fbeb8b0b596e1f5a5c629b77a45183')
mgr = owm.weather_manager()

# You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot(
    "1543860384:AAFvMfIsiv8Nr4_Z9v5w7Yp5ynjnDd6nWJ4", parse_mode=None)


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "In " + message.text + " now " + "\n"
    answer += str(temp) + " celsius degree and " + \
        str(w.detailed_status) + "\n"

    if temp < 10:
        answer += "Put on worm clothes"
    elif temp < 20:
        answer += "Now is cold"
    else:
        answer += "Temperature is norm"


# bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
