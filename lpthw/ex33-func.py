#! /usr/bin/python

numbers = []
i = 0

def add_num(count, gap) :
	i = 0
	while i < count :
		print "At the top i is %d " % i
		print "Current Number to be entered is : %d " % i
		numbers.append(i)
	
		i += gap
		print "Numbers now ", numbers
		print "At the bottom i is %d " % i

add_num(5, 2)
print "The numbers "

for num in numbers :
	print num
	
