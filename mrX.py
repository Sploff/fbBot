import config, brain, eventPlans, pdb, threading
from fbchat import Client
from fbchat.models import *
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
#pdb.set_trace()


#client.send(Message(text='<message>'), thread_id='<user id>', thread_type=ThreadType.USER)
#client.send(Message(text='<message>'), thread_id='<group id>', thread_type=ThreadType.GROUP)
def sendMsg(user,msg,tType='user'):
	if tType == 'user':
		client.send(Message(text=msg), thread_id=brain.USERS[user], thread_type=ThreadType.USER)
	else:
		client.send(Message(text=msg), thread_id=brain.GROUPS[user], thread_type=ThreadType.GROUP)

def goto(user,pos,date_time):
	msg= "Infinn dig! ({})\n{}".format(str(date_time),brain.POS[pos])
	sendMsg(user,msg)


stupid_translator= {
	'goto': goto,
	'sendMsg': sendMsg
}

def my_job(text):
	print(text)



def startEvents():
	print("START")
	sched = BlockingScheduler()
	for plan in eventPlans.TILL_JOBB:
		sched.add_job(stupid_translator[plan[1]], 'date', run_date=plan[0], args=plan[2])
	sched.start()

t = threading.Thread(target=startEvents)
t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
t.start()



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

		#self.markAsDelivered(author_id, thread_id)
		#self.markAsRead(author_id)
		if message_object.text.lower() == (listenPrefix + 'help'):
			client.send(Message(text='- help\n- version\n- next date\n- calendar'), thread_id=thread_id, thread_type=thread_type)
		elif message_object.text.lower() == (listenPrefix + 'version'):
			client.send(Message(text=mrxVersion), thread_id=thread_id, thread_type=thread_type)
		elif message_object.text.lower() == listenPrefix + 'next date':
			client.send(Message(text=brain.HKX['DATES'][brain.HKX['NEXT_DATE'][0]][brain.HKX['NEXT_DATE'][1]]), thread_id=thread_id, thread_type=thread_type)
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
def sendMsg2(user,msg,tType='user'):
	if tType == 'user':
		client.send(Message(text=msg), thread_id=brain.USERS[user], thread_type=ThreadType.USER)
	else:
		client.send(Message(text=msg), thread_id=brain.GROUPS[user], thread_type=ThreadType.GROUP)

def goto2(user,pos,dateTime):
	msg= "Infinn dig! ({})\n{}".format(dateTime,brain.POS[pos])
	sendMsg(user,msg)


def logout():
	client.logout()


if __name__ ==  '__main__':
	client.listen()
	#pdb.set_trace()
	pass
