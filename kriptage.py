#loop.add_signal_handler(signal.SIGINT, stop)
"""Sample Slack ping bot using asyncio and websockets."""
import asyncio
import json
import signal
import sys
import aiohttp
import websockets
from slackclient import SlackClient


DEBUG = True
TOKEN = "xoxb-38220681028-zv6LPDJeLEOwq4q8qHPGFFOQ"
RUNNING = True
sc = SlackClient(TOKEN)
print(sc.api_call("api.test"))

d = {"/print" : getWarning, "/subme" : subscribe}


async def consumer(message):
    """Display the message."""
    if message.get('type') == 'message':
        user = await api_call('users.info',
                              {'user': message.get('user')})

        #print("{0}: {1}".format(user["user"]["name"],
        #                        message["text"]))
        d[message["text"]]
    else:
        print(message, file=sys.stderr)

async def bot(token=TOKEN):
    """Create a bot that joins Slack."""
    rtm = await api_call("rtm.start")
    assert rtm['ok'], "Error connecting to RTM."

    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(rtm["url"]) as ws:
            async for msg in ws:
                assert msg.tp == aiohttp.MsgType.text
                message = json.loads(msg.data)
                asyncio.ensure_future(consumer(message))
