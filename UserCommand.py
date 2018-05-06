import brain

class UserCommand:
	def __init__(self, user_id, content):
		self.user_id= user_id
		self.user_name= self.get_user_name()
		self.content= self.filter_content(content)

	def get_user_name(self):
		for user in brain.USERS:
			if brain.USERS[user] == self.user_id:
				return user
		return None

	def filter_content(self, content):
		if content.text:
			return content.text.lower()
		return None
			



	##############
	###   IS   ###
	##############
	def is_super_user(self):
		if self.user_name in brain.GROUPS['SUPER-USERS']:
			return True
		return False

	def is_admin(self):
		if self.user_name in brain.GROUPS['SUPER-USERS'] or self.user_name in brain.GROUPS['ADMINS']:
			return True
		return False

	def is_user(self):
		if self.user_name in brain.GROUPS['SUPER-USERS'] or self.user_name in brain.GROUPS['ADMINS'] or self.user_name in brain.GROUPS['USERS']:
			return True
		return False

	def is_in_content(self, triggers):
		for trigger in triggers:
			if trigger in self.content:
				return True
		return False
