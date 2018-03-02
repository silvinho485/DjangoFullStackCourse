from bottery import Bottery
import Calendar
import mother_jokes
from Dictionary_requests import result, elsa
bot = Bottery()

@bot.patterns.message('ping')
def pong(message):
    return 'pong'

@bot.patterns.message('#hola')
def hola(message):
    return Calendar.bot()

@bot.patterns.message('#mamae')
def mamae(message):
    return mother_jokes.xingar()

@bot.patterns.message('#papai')
def papai(message):
    return 'VSF! Que já depositei a pensão desse mês.'

@bot.patterns.startswith('#dict')
def dicto(message):
    if len(message.text.split(' ')) > 1:
        word = message.text.split(' ')[1]
        word = result(word)
    elif len(message.text.split(' ')) > 2:
        word = elsa()
    else:
        word = elsa()
    return word

