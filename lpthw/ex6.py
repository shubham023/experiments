#! /usr/bin/python

x = "There are %d kind of people" % 10;

binary = "binary"
dont ="dont"
y = "Those who knows %s and those who %s"% (binary, dont)

print "I said %r"% x
print "I also said '%s'"% y

hillarious = False
joke_eval = "Isn't that joke so funny ! %r"

print joke_eval % hillarious

left = "<---- This is the left side of text"
right = " ----> This is the right side of text"

print left+right



