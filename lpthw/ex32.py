#! /usr/bin/python

number = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'papaya', 'grapes', 'banana']
change = [1, 'roti', 2, 'kapda', 3, 'makan']

for num in number :
	print "Number is %d" % num

for fruit in fruits :
	print "Fruit currentley selected is : %s" % fruit

for i in change :
	print "I is %r" % i

elements = []

for i in range (0, 10) :
	print "Appending %d " % i
	elements.append(i)

for i in elements :
	print "Element is : %d " % i
