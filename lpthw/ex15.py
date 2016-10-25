#! /usr/bin/python

from sys import argv

txt = open("ex15_sample.txt")
print "Printing the file after having the filename in the program itself "
print txt.read()
txt.close()

script, filename = argv
txt_again = open(filename)
print "Script %s will print the file %s" % (script, filename)
print txt_again.read()
txt_again.close()
