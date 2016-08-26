#! /usr/bin/python

from sys import argv 

script, filename = argv

def readFile(f):
	print f.read()

def rewindFile(f):
	f.seek(0)

def printLine(f):
	print f.readline()


print "Let's first print all the lines from file \n"

file_handle = open(filename)
readFile(file_handle)
rewindFile(file_handle)

printLine(file_handle)
printLine(file_handle)
printLine(file_handle)



#readFile(file_handle)
