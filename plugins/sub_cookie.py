from . import bot


@bot.subscribe('cookie')
def sub_cookie(message):
    bot.speak('I see a cookie in "{0}"'.format(message['text']))
