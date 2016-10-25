#! /usr/bin/python

print "Hello"

printLine = """
	Printing the whole text
	without changing the indentation.
printing multiple lines without changing anything 
"""
print printLine

calculation = 10 + 2 - 3 / 2
print "Calculation is : %d " % calculation

def function1(myString, myNum):
	print "String sent to function is : %s and digit sent is %d " % (myString, myNum)
	retString = "Hello" + myString	
	retNum = myNum + 2
	return retString, retNum


getString, getNum = function1("Shubham", 2)

print "String returned is : %s and number returned is : %d" % (getString, getNum)

