from __future__ import print_function
from glob import glob
import importlib


bot = None

def init_plugins(bot_):
    global bot
    bot = bot_

    for plugin in glob('plugins/[!_]*.py'):
        try:
            importlib.import_module(plugin.replace('/', '.')[:-3])
        except Exception as e:
            print('Failed to import {1}: {2}'.format(plugin, e))
