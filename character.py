class Character():

	# Create a character
	def __init__(self, char_name, char_description):
		self.name = char_name
		self.description = char_description
		self.conversation = None
		self.tickle_reaction = None
		self.holding = None

	# Describe this character
	def describe(self):
		print( self.name + " is here!" )
		print( self.description )

	# Set what this character will say when talked to
	def set_conversation(self, conversation):
		self.conversation = conversation

	# Talk to this character
	def talk(self):
		if self.conversation is not None:
			print("[" + self.name + " says]: " + self.conversation)
		else:
			print(self.name + " doesn't want to talk to you")
	
	# Sets the reaction when tickled
	def set_tickle_reaction(self, reaction):
		self.tickle_reaction = reaction

	# Set what the charcter is holding
	def set_holding(self,holding):
		self.holding = holding

	# Fight with this character
	def fight(self, combat_item):
		print(self.name + " doesn't want to fight with you")
		return True

	# Tickle the character
	def tickle(self):
		print("You tickle " + self.name + " and " + self.tickle_reaction + ".")
		print(self.name + " drops a " + self.holding + ".")

class Enemy(Character):

	def __init__(self, char_name, char_description):
		super().__init__(char_name, char_description)
		self.weakness = None
	def get_weakness(self):
		return self.weakness
	def set_weakness(self, char_weakness):
		self.weakness = char_weakness
	def fight(self, combat_item):
		if combat_item == self.weakness:
			print("You fend " + self.name + " off with the " + combat_item )
			return True
		else:
        		print(self.name + " crushes you, puny adventurer")
        		return False

class Friend(Character):

	def __init__(self, char_name, char_description):
		super().__init__(char_name, char_description)
		self.heal = None
