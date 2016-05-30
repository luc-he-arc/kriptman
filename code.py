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

def getChannel(userID):
    chan = sc.api_call("im.open", user=userID)
    return chan['channel']['id']

def sendMessage(chan, txt):
    sc.api_call("chat.postMessage", as_user="true", channel=chan, text=txt)

plan = { "2016.7.3" : { "INF2dlm-a" : { "C++ avec Qt" : "X" , "Projet P2 conception" : "p"},
						"INF2dlm-b" : { "C++ avec Qt" : "X" , "Projet P2 conception" : "p"},
					  },
		 "2016.7.4" : { "INF2dlm-a" : { "Projet P2 conception" : "p"},
						"INF2dlm-b" : { "Application web" : "p" , "Réseaux et applications" : "p" ,"Projet P2 conception" : "p"},
					  },
		 "2016.7.5" : { "INF2dlm-a" : { "Application web" : "p" , "Projet P2 conception" : "p"},
						"INF2dlm-b" : { "Projet P2 conception" : "p"},
					  }
	   }

sub = { "INF2dlm-a" : { "U0MN8R6NA"},
		"INF2dlm-b" : {},
		"C++ avec Qt" : {},
		"Projet P2 conception" : {},
		"Application web" : {},
		"Réseaux et applications" : {}
	  }


#{ eleve1 : { "C++ avec Qt" : "X", "Projet P2 conception" : "p" },
#  eleve2 : ...
def sendRappel(eleve, classe, cours):
	print(eleve)
	user = sc.api_call('users.info', user=eleve)
	print(user)
	sendMessage(getChannel(user["user"]["id"]), formatMessage(classe, cours))

#sendRappel("2016.7.3")


def autre(date):
	for classe in plan[date]:
		for eleve in sub[classe]:
			#print(eleve + classe)
			sendRappel(eleve, classe, plan[date][classe])
		for cours in plan[date][classe]:
			for eleve in sub[cours]:
				#print(eleve + classe + cours)
				test = {cours : plan[date][classe][cours]}
				sendRappel(eleve, classe, test)

def formatMessage(classe, cours):
	d = {"X" : "une evalution !", "p" : "le projet à continuer"}
	message = "Bonjour, avec la classe "+classe+","
	print(cours)
	for nom in cours:
		message += "en "+nom+", vous avez "+d[cours[nom]]+"\n"
	return message


autre("2016.7.3")
