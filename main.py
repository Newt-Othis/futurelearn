from room import Room
from character import Enemy

# Set up room names, descriptions and connections
kitchen = Room("Kitchen")
dining_hall = Room("Dining hall")
ballroom = Room("Ballroom")

kitchen.set_description("A dank and dirty room buzzing with flies.")
dining_hall.set_description("Clean and tidy, but smelling faintly of cabbage.")
ballroom.set_description("There is a dusty dancefloor here, lit through dirty, cobwebby windows.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Set up characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dave.set_tickle_reaction("his arm falls off. Dave picks it up.")
dave.set_holding("sandwich")
dining_hall.set_character(dave)

autumn = Enemy("Autumn","A small monster.")
autumn.set_conversation("I done a wee wee!")
autumn.set_weakness("curry")
autumn.set_tickle_reaction("she laughs!")
autumn.set_holding("banana")
ballroom.set_character(autumn)

# Set initial room
current_room = kitchen

while True:
	# print("\n")
	print("")
	current_room.get_details()
	print("")
	inhabitant = current_room.get_character()
	if inhabitant is not None:
		inhabitant.describe()
		print("")
	command = input("> ")
	print("")
	
	# Check whether a direction was typed
	if command in ["north", "south", "east", "west"]:
		current_room = current_room.move(command)
	
	elif command == "talk":
		if inhabitant is not None:
			inhabitant.talk()
		else:
			print("You talk to an empty room...")
	
	elif command == "tickle":
		if inhabitant is not None:
			inhabitant.tickle()
		else:
			print("There's nobody to tickle")
	
	elif command == "fight":
		weapon = input("Fight with what? > ")
		print("")
		if inhabitant is not None:
			#inhabitant.fight(weapon)
			if inhabitant.fight(weapon)== False:
				print ("\n")
				print("You dead!")
				exit()
			else:
				#enemy defeated
				current_room.set_character(None)
		else:
			print("You wave the " + weapon + " around.")
