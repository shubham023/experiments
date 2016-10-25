#! /usr/bin/python

def add(a, b):
	print "ADDITION of %d and %d is in progress " % (a,b)
	return a + b

def substract(a, b):
	print "SUBSTRACTION of %d and %d is in progress " % (a,b)
	return a - b

def multiplication(a, b):
	print "MULTIPLICATION of %d and %d is in progress " % (a, b)
	return a * b

def division(a, b):
	print "DIVISION of %d and %d is in progress" % (a,b)
	return a / b

age = 25
height = 168

age = add(age, 2)
height = substract(height, 2)
weight = multiplication(age,3)
iq = division(weight + height + weight, 3)

print "Age is : %d and Height is : %d and Weight is : %d and iq is : %d" % (age, height, weight, iq)

