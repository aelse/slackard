#!/usr/bin/env python

import functools
import slacker
import yaml
import importlib
from glob import glob
import time


bot = None


class Config(object):
    config = {}

    def __init__(self, file_):
        f = open(file_, 'r')
        y = yaml.load(f)
        f.close()
        self.__dict__.update(y)


class Slackard(object):

    subscribers = []
    commands = []
    firehoses = []

    def __init__(self, config_file):
        self.config = Config(config_file)
        self.apikey = self.config.slackard['apikey']
        self.botname = self.config.slackard['botname']
        self.botnick = self.config.slackard['botnick']
        self.channel = self.config.slackard['channel']

        self._import_plugins()

    def __str__(self):
        return 'I am a Slackard!'

    def _import_plugins(self):
        for plugin in glob('plugins/[!_]*.py'):
            try:
                importlib.import_module(plugin.replace('/', '.')[:-3])
            except:
                print 'Failed to import {0}'.format(plugin)

    def _init_connection(self):
        self.slack = slacker.Slacker(self.apikey)
        r = self.slack.channels.list(self.channel)
        assert(r.successful)
        c_map = {c['name']: c['id'] for c in r.body['channels']}
        self.chan_id = c_map[self.channel]

    def _fetch_latest_messages(self, since=None):
        r = self.slack.channels.history(self.chan_id)

    def say(self, message):
        self.slack.chat.post_message(self.channel, message,
                                     username=self.bot_name,
                                     icon_url=self.bot_icon)

    def run(self):
        self._init_connection()

        h = self.slack.channels.history(self.chan_id, count=1)
        assert(h.successful)
        ts = float(h.body['messages'][0]['ts'])
        print 'Found initial ts {0}'.format(ts)
        t0 = time.time()

        while True:
            t1 = time.time()
            delta_t = t1 - t0
            if delta_t < 10.0:
                print 'sleep {0}'.format(10.0 - delta_t)
                time.sleep(10.0 - delta_t)
            else:
                print 'no sleep'
            t0 = t1

            h = self.slack.channels.history(self.chan_id, oldest=ts)
            assert(h.successful)
            ts = float(h.body['messages'][0]['ts'])
            print 'Found new ts {0}'.format(ts)
            messages = h.body['messages']
            messages.reverse()
            for message in messages:
                if float(message['ts']) != ts:
                    print message['text']
                    for firehose in self.firehoses:
                        firehose(message['text'])

    def subscribe(self, wrapped, message_prefix):
        @functools.wraps(wrapped)
        def _f(*args, **kwargs):
            return wrapped(*args, **kwargs)

        self.subscribers.append((_f, message_prefix))
        return _f

    def command(self, wrapped, command):
        @functools.wraps(wrapped)
        def _f(*args, **kwargs):
            return wrapped(*args, **kwargs)

        self.commands.append((_f, command))
        return _f

    def firehose(self, wrapped):
        @functools.wraps(wrapped)
        def _f(*args, **kwargs):
            return wrapped(*args, **kwargs)

        self.firehoses.append(_f)
        return _f


def main():
    bot = Slackard('slackard.yaml')
    bot.run()


if __name__ == '__main__':
    main()
