import config, brain, eventPlans, pdb, threading, time
from fbchat import Client
from fbchat.models import *
from UserCommand import UserCommand
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
#pdb.set_trace()


#client.send(Message(text='<message>'), thread_id='<user id>', thread_type=ThreadType.USER)
#client.send(Message(text='<message>'), thread_id='<group id>', thread_type=ThreadType.GROUP)
def sendMsg(includeUsers, excludeUsers, msg):
	print("sendMsg()")
	users= []
	for i_user in includeUsers:
		if i_user in brain.GROUPS:
			for usr in brain.GROUPS[i_user]:
				users.append(brain.USERS[usr])
		elif i_user in brain.USERS:
			users.append(brain.USERS[i_user])
	for e_user in excludeUsers:
		if e_user in brain.USERS:
			users.pop(users.index(brain.USERS[e_user]))

	for user in users:
		client.send(Message(text=msg), thread_id=user, thread_type=ThreadType.USER)
		time.sleep(.5)

def goto(includeUsers, excludeUsers, pos, date_time, extra_text=""):
	print("goto()")
	msg= "Var på följande position senast: {}\n{}\n{}".format(str(date_time),brain.POS[pos],extra_text)
	sendMsg(includeUsers, excludeUsers, msg)

def mission(includeUsers, excludeUsers, mission, args=[]):
	try:
		missions= {
			"give_beer": "Mr X says, Give someone {} sips".format(args[0])
		}
	except:
		print("Exception: mission()")


stupid_translator= {
	'goto': goto,
	'sendMsg': sendMsg
}

def my_job(text):
	print(text)



def eventHandler():
	print("START")
	sched = BlockingScheduler()
	for plan in eventPlans.HKX:
		sched.add_job(stupid_translator[plan[1]], 'date', run_date=plan[0], args=plan[2], timezone="Europe/Paris")
	sched.start()

t = threading.Thread(target=eventHandler)
t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
t.start()



class MrxClient(Client):
	user_cmd= None

	def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
		user_cmd= UserCommand(author_id, message_object)
		listenPrefix= "mrx "
		mrxVersion= "0.1"
		# Do something with message_object here
		#print("mid: " + str(mid))
		print("\n\nauthor_id: " + str(author_id))
		print("message_object: " + str(message_object))
		print("thread_id: " + str(thread_id))
		print("thread_type: " + str(thread_type))
		#print("ts: " + str(ts))
		#print("metadata: " + str(metadata))
		#print("msg: " + str(msg))

		#self.markAsDelivered(author_id, thread_id)
		#self.markAsRead(author_id)
		#pdb.set_trace()
		if user_cmd and user_cmd.content and user_cmd.user_name != 'MrX':
			if 'help' in user_cmd.content and user_cmd.is_user():
				client.send(Message(text='- help\n- version\n- next date\n- calendar\n- commands'), thread_id=thread_id, thread_type=thread_type)
			elif 'commands' in user_cmd.content and user_cmd.is_admin():
				client.send(Message(text=(
					'- get users\n'
					'- get groups\n'
					'- get pos\n'
					'*- add user <username> <fb id>\n'
					'*- add pos <name> <url>\n'
					'*- add goto [<users/group>] [<exclude users>] <pos> <when to send> <when to be there> \n'
					'*- add msg [<users/group>] [<exclude users>] <msg>\n'
					'* not implemented yet\n'
				)), thread_id=thread_id, thread_type=thread_type)
			elif 'version' in user_cmd.content:
				client.send(Message(text=brain.INFO['VERSION']), thread_id=thread_id, thread_type=thread_type)
			elif 'next date' in user_cmd.content and user_cmd.is_user():
				client.send(Message(text=brain.HKX['DATES'][brain.HKX['NEXT_DATE'][0]][brain.HKX['NEXT_DATE'][1]]), thread_id=thread_id, thread_type=thread_type)
			elif 'calendar' in user_cmd.content and user_cmd.is_user():
				client.send(Message(text=brain.HKX['CALENDAR']), thread_id=thread_id, thread_type=thread_type)
			elif '2018' in user_cmd.content and user_cmd.is_user():
				strOut= ""
				for date in brain.HKX['DATES']['2018']:
					strOut+= "{}\n".format(date)
				client.send(Message(text=strOut), thread_id=thread_id, thread_type=thread_type)
			elif 'get users' in user_cmd.content and user_cmd.is_admin():
				users= []
				for user in brain.USERS:
					users.append(user)
				client.send(Message(text=str(users)), thread_id=thread_id, thread_type=thread_type)
			elif 'get groups' in user_cmd.content and user_cmd.is_admin():
				groups= ""
				for group in brain.GROUPS:
					groups+="{}:\n{}\n".format(str(group), str(brain.GROUPS[group]))
				client.send(Message(text=groups), thread_id=thread_id, thread_type=thread_type)
			elif 'get pos' in user_cmd.content and user_cmd.is_admin():
				positions= ""
				for pos in brain.POS:
					positions+= "{}: {}\n".format(pos, brain.POS[pos])
				client.send(Message(text=positions), thread_id=thread_id, thread_type=thread_type)
		elif 'latitude' in str(msg) and 'longitude' in str(msg):
			latitude= str(msg).split("{'latitude': ")[1].split(", 'longitude': ")[0]
			longitude= str(msg).split(", 'longitude': ")[1].split("}, ")[0]
			client.send(Message(text=str(latitude)+", "+str(longitude)), thread_id=thread_id, thread_type=thread_type)
			
		#except Exception as e:
		#	print("Exception in onMessage(): " + e)


#print(config.FACEBOOK['EMAIL'])
#print(config.FACEBOOK['PASSWORD'])

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
