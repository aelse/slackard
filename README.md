# slackard

A Slack bot (slack.com)

Slackard listens to the configured channel and is capable of responding to
message events occurring in that channel.

## Configuration

See the included slackard.yaml configuration file for supported options.
All are required except boticon and botemoji, which are both optional. If
both are provided then botemoji will override boticon (per the Slack API).

## Plugins

A basic plugin system enables you to add whatever functionality you need to
your bot. You may wish for it to respond to particular commands, or to
listen for certain words, or even watch the entire channel conversation.

Slackard provides decorators supporting 3 types of registration to suit your
need. In all cases the only messages passed will be those not produced by
the bot itself. This is to avoid getting stuck in message read-respond loops.

Examples are included in the plugins directory.

### Command

This provider allows you to process specific commands directed at the bot by
name. eg. If the configuration set a botnick of 'slack', then
'slack: say Hello world' would pass 'Hello world' to anything that has
subscribed to the command 'say'.

```python
@bot.command('say')
def command_say(args):
    bot.speak('You asked me to say, "{0}"'.format(args))
```

### Subscribe

The plugin subscribes to a particular pattern. This is any pattern that can
be passed through re.compile, and is applied to each message received by the
bot. If a message matches then the entire message is passed.

```python
@bot.subscribe('cookie')
def sub_cookie(message):
    bot.speak('I see a cookie in "{0}"'.format(message['text']))
```

### Firehose

The plugin receives a full feed of channel traffic.

```python
@bot.firehose
def listen(message):
    # Do something with `message`
    pass
```

## License


BSD 2-Clause License

Copyright (c) 2012-2014, Alexander Else All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
