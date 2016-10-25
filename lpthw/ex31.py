#! /usr/bin/python

print "You are in a dark room with 2 doors. Lets us know which door you want to open #1 or #2 ? "

door = raw_input(">")

if door == "1" :
	print "There is a bear inside the room with a cake what will you do now ? "
	print "1. Eat the cake from bear"
	print "2. Scream at the bear"
	
	bear = raw_input(">")
	if bear == "1" :
		print "Bear will eat your face"
	elif bear == "2" :
		print "Bear will cut your leg and eat it"
	else : 
		print "Well Done! , Bear will be killed with this option i.e. %s " % bear
elif door == "2" :
	print "Now you have 3 options"
	print "1. Sleep"
	print "2. Watch movies"
	
	choice = raw_input("<")
	if choice == "1" :
		print "Sleeping is good for getting refreshed"
	elif choice == "2" : 	
		print "Watch some good movie atleast"
	else : 
		print "What ? Wanna play some game??? "

else :
	print "You cant do anything, get out of the room! "
