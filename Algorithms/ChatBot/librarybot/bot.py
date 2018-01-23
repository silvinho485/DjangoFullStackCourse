from bottery import Bottery
import Calendar
import mother_jokes

bot = Bottery()

@bot.patterns.message('ping')
def pong(message):
    return 'pong'

@bot.patterns.message('#hola')
def pong(message):
    return Calendar.bot()

@bot.patterns.message('#mamae')
def pong(message):
    return mother_jokes.xingar()
