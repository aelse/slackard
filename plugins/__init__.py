from glob import glob
import importlib


bot = None

def init_plugins(bot_):
    global bot
    bot = bot_

    for plugin in glob('plugins/[!_]*.py'):
        try:
            importlib.import_module(plugin.replace('/', '.')[:-3])
        except Exception, e:
            print 'Failed to import {0}: {1}'.format(plugin, e)
