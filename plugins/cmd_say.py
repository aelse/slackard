from plugins import bot


@bot.command('say')
def command_say(args):
    bot.speak('You asked me to say, "{0}"'.format(args))
