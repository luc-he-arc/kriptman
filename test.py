from code import api_call, getChannel, sendMessage, sendRappel, formatMessage, safe_list_get

import pytest
import asyncio
from asynctest import patch

import unittest

#malgrès 3 heure de lecture de documentation python
#les test asynchrone ne fonctionne toujours pas
#cependant, la logique est là
#il faudra essayer de rendre ces tests fonctionnels avec l'aide de l'enseigant

@pytest.mark.asyncio
@asyncio.coroutine
def test_api_call():
    rtm = yield from api_call("rtm.start")
    assert rtm['ok'], "Error connecting to RTM."

@pytest.mark.asyncio
@asyncio.coroutine
def test_get_channel_of_U0MN8R6NA():
    user_id = "U0MN8R6NA"
    channel = await getChannel(user_id)
    assert (channel, "D1472HSR5")

@pytest.mark.asyncio
@asyncio.coroutine
def test_sendMessage_on_channel_D1472HSR5():
    channel = "D1472HSR5"
    print(await sendMessage(channel, "bonjour"))
    #assert(await sendMessage(channel, "bonjour"), )

@pytest.mark.asyncio
@asyncio.coroutine
def test_sendRappel_to_U0MN8R6NA():
    user_id = "U0MN8R6NA"
    classe = "INF2dlm-a"
    cours = { "C++ avec Qt" : "X" , "Projet P2 conception" : "p"}

    print(await sendRappel(user_id, classe, cours))
    #assert(await sendRappel(user_id, classe, cours), )

#les deux test suivants n'ont pas besoin d'asynchrone
class MyTest(unittest.TestCase):
    def test_formatMessage_of_INF2dlm_2(self):
        classe = "INF2dlm-a"
        cours = {"Projet P2 conception" : "p",  "C++ avec Qt" : "X" }
        assert(formatMessage(classe,cours), "Bonjour, avec la classe INF2dlm-a,en Projet P2 conception, vous avez le projet à continuer\n" + \
                                            "en C++ avec Qt, vous avez une evalution !")

    def test_safe_list_get_date_or_default(self):
        list1 = ["print","2016.7.3"]
        list2 = ["print"]

        result1 = safe_list_get(list1, 2, "default")
        result2 = safe_list_get(list2, 2, "default")

        assert(result1, "2016.7.3")
        assert(result2, "default")
