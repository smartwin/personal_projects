import sys from exit

class Room(object):
	
	def enter():
		print "This room does not exist, you cannot not enter!!"
		exit(1)


class Office(object):

	def __init__(self, room_direct):
		self.room_direct = room_direct

	def play(self):
		current_room = self.room_direct.first_room()
		last_room = self.room_direct.next_room('freedom')

		while current_room != last_room:
			next_room_name = current_room.enter()
			current_room = self.room_direct.next_room(next_room_name)

		current_room.enter() 

class Death(Room):
	quips = [
		"You died. You kinda suck at this.",
		"You mom would be proud...if she were smarter.",
		"Such a luser",
		"I have a small puppy that's better at this"
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(0)

class FoodCourt(Room):

	def enter(self):
		print """
			The time has finally come. The zombies have found their way into the mall.
			Whether it's God or luck, you have also found your ticket to salvation. A
			helicopter is on its way to take you and your team to sancuuary. You guys just
			have to out run the zombies and make it to the roof.
			\n
			AS the leader of the team it is your decision to decide how everyone makes it
			to the roof alive and unaffected.
			"""

		action = raw_input('> ')

		if action == "run for the roof":

		print """
			You assumed wrong thinking your whole group can outrun the zombies. 
			Being the leader of your group, you stay at the back of the group 
			making sure everyone stay together. This is you demise. As you're trying to help
			the weakest link, a zombie clips your leg, causing you to fall. The zombies crawl 
			on top of you and the last things you see as you are eaten are the memebers of your group
			fall like domino pieces as zombies eat them one by one.
			"""
			return 'death'

		elif action == "get weapons"

			print """
				Because you know your group cannot out run the zombies, you make the smart choice and make a 
				run for Dick's first, where you know you can stack up on weapons. While this will allow the
				zombies to get to other parts of the mall, you also know this is your best bet for survivial.
				You direct your team towards Dick's, with the zombies on your heels, but getting their fast
				enough to pull down the security gate. This temporarily blocks out the zombies.
				"""
			return 'dicks'

		else:

			print "That is not possible in this scenario"
			return 'food_court'

class Dicks(Room):

	def enter(self):

		print """
			While at Dicks, you gather all the weapons you will need for zombies inside and outside of the mall.
			You now have to decide how your team will make it out of the store. While the only exit is the way you
			came in, you know you have to startegize the best way to get out. All eyes are on you...
			"""

		action = raw_input('> ')

		if action == "lift gates":
		
			print """
			Halfway up the gate jams, allowing the zombies out, but keeping the team trapped.
			While you are able to kill the front row of zombies, your team is not quick enough to
			reload and kill the next hoarde of zombies. One by one, members of you team are eaten.
			AS you are the last one to die, you die to the screams of your members being eaten.
			"""
			return 'death'

		elif action == "blowout the gates":

			print """
				While you were successfully able to blow away the gate and the zombies standing in front
				of it, clearing your way out of the store. The blowback from the explosion also kills
				you as well. You are not fried dinner for the zombies remaining in the rest of the
				mall. 
			"""
			return 'death'

		elif action == "ram the gates"

			print """
				Because Dick's has everything, you find off course humvees sitting in the back. They have
				enough gas to make it through the gate and pass the zombies standing in front of the gate.
				In a traingle formation, you and your team drive four humvees through the gate, clearing
				enough of a path for you guys to make it to Macys, which will give you access to the roof.
				"""
			return 'macys'

		else:
			print "That is not an option in this scenario"
			return 'dicks'

class Macys(Room):

	def enter(self):
		print """
			Now that you are in Macys, your right hand confess that there is only room for 5 people on 
			the helicopter. There is 7 of you guys in the group. Therefore you must decide how to sacrifice
			two people in order to ensure the majority of the people make it saftey.
			"""

		action = raw_input('> ')

		if action == "split up":
		
			print """
				You decide to split of the group in groups of 2, with you being the odd man out. You know that being
				the leader, you will make it to the roof first allowing you to shut the door on the remaining team 
				memebers allowing the strongest to survive. This plan backfires, becuase no one has actually been in 
				the Macys since the apocalypse started, causing everyone to not be able to find the door that leads to
				the roof. The zombies eventually catch up to you guys and kill off each member of the team. Being
				alone you eventually see the door to the roof, but right before you reach it, you are tackled by
				a zombie and eaten. 
				"""
			return 'death'

		elif action == "take the risk":
		
			print """
				You decide to take the risk and lead all 7 members up to the roof. You make the right decision and 
				every memeber is able to fit on the helicopter safely. The helicopter is able to take off right at
				the knick of time, barely missing the zombies rushing the roof access door.
				"""
			return 'take_off'

		elif action == "make decision":
			print """
				You decide to make the decision of killing off the necessary 2 people right when you guys enter Macys.
				After you fire off the shots, a coup/gunfight breaks out calling for justice of the two people killed.
				Every member is shot and killed, since there is no law and order. You die with regret and guilt and a little
				shame it wasn't by zombies, but by the third weakest link.
				"""
			return 'death'

class Roof(Room):

	def enter(self):
		print "You have made it out of the mall safely. You are finally able to relax and make it saftey. You win"

class Directory(object):

	rooms = {
		'food_court' : FoodCourt(),
		'dicks' : Dicks(),
		'macys' : Macys(),
		'take_off' : Roof(),
		'death' : Death(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_room(self, scene_name):
		val = Directory.rooms.get(room_name)
		return val

	def opening_room(self):
		return self.next_room(self.start_room)

a_map = Directory('food_court')
a_game = Office(a_room)
a_game.play()