#! /usr/bin/python

numbers = []
i = 0

while i < 6 :
	print "At the top i is %d " % i
	print "Current Number to be entered is : %d " % i
	numbers.append(i)
	
	i += 1
	print "Numbers now ", numbers
	print "At the bottom i is %d " % i

print "The numbers "

for num in numbers :
	print num
	
