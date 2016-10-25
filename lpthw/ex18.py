#! /usr/bin/python

def print_two(*args):
	arg1, arg2 = args
	print "arg1 is : %r and arg2 is : %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "here is arg1 : %r and here is arg2 : %r" % (arg1,arg2)

def print_one(arg1):
	print "arg1 is : %r" % arg1

def print_none():
	print "Nothing given to me"

print_two("hello","How") 
print_two_again("hello", "again")
print_one("Hello")
print_none()
