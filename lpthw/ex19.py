#! /usr/bin/python

def checkParty(cheese_count, guest_count):
	if cheese_count >= guest_count :
		print "Party is possible :) \n"
	else:
		print "Party is NOT possible :( \n"

# This is for making party possible
cheese_count=21
guest_count=16
checkParty(29,29)
checkParty(cheese_count,guest_count)
checkParty(cheese_count-10,guest_count+2)
