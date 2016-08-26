#! /usr/bin/python
from sys import exit

def gold_room() :
	print "This room is full of gold! Let me know how much you want"
	next = raw_input("<")
	
	if "0" in next or "1" in next :
		how_much = int(next)
	else :
		dead("You dont know how to type numerals")

	if how_much < 50 :
		print "you are not greedy"
		exit(0)
	else :
		dead ("So much greedy!!!")

def bear_room() :
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True :
		next = raw_input("<")
		if next == "take honey" :
			dead("Dont you take honey! bear killed you!!")
		elif next == "taunt bear" and not bear_moved :
			print "That was nice, bear has moved now !! "
			bear_moved = "True"
		elif next == "taunt bear" and bear_moved : 
			dead("bear has already moved and you are taunting.. So bear will eat you !!!")
		elif next == "open door" and bear_moved :
			gold_room()
		else : 
			print "Not sure what you wanna do!!"

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input("<")
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why, "Well Played!!"
	exit(0)

def start() :
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input("<")
	
	if next == "left" :
		bear_room()
	elif next == "right" : 
		cthulhu_room()
	else :
		dead("You dont know what you wanna do")

start()
