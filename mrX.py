import config, brain, pdb
from fbchat import Client
from fbchat.models import *


class MrxClient(Client):
	def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
		listenPrefix= "mrx "
		mrxVersion= "0.1"
		# Do something with message_object here
		#print("mid: " + str(mid))
		print("author_id: " + str(author_id))
		print("message_object: " + str(message_object))
		print("thread_id: " + str(thread_id))
		print("thread_type: " + str(thread_type))
		#print("ts: " + str(ts))
		#print("metadata: " + str(metadata))
		#print("msg: " + str(msg))

		self.markAsDelivered(author_id, thread_id)
		self.markAsRead(author_id)
		if message_object.text.lower() == (listenPrefix + 'version'):
			client.send(Message(text=mrxVersion), thread_id=thread_id, thread_type=thread_type)
		if message_object.text.lower() == listenPrefix + 'next date':
			client.send(Message(text='180609?'), thread_id=thread_id, thread_type=thread_type)
		elif message_object.text.lower() == listenPrefix + 'calendar':
			client.send(Message(text=brain.HKX['CALENDAR']), thread_id=thread_id, thread_type=thread_type)
		pass


print(config.FACEBOOK['EMAIL'])
print(config.FACEBOOK['PASSWORD'])

client= MrxClient(config.FACEBOOK['EMAIL'], config.FACEBOOK['PASSWORD'])

def getIds():
	for thread in threads:
		print(thread['id'])


def login():
	if not client.isLoggedIn():
		client.login(config.FACEBOOK['EMAIL'], config.FACEBOOK['PASSWORD'])


#client.send(Message(text='<message>'), thread_id='<user id>', thread_type=ThreadType.USER)
#client.send(Message(text='<message>'), thread_id='<group id>', thread_type=ThreadType.GROUP)
def sendMsg(user,msg):
	client.send(Message(text=msg), thread_id=config.USERS[user], thread_type=ThreadType.USER)

def logout():
	client.logout()


if __name__ ==  '__main__':
	client.listen()
	#pdb.set_trace()
