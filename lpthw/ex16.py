#! /usr/bin/python

from sys import argv

script, filename = argv

print "Hello There ! I am going to delete %s "% filename
print "If you dont want to delete then press ctrl-c "

raw_input("If you want to delete then press enter")

file_handle = open(filename,'w')
file_handle.truncate()

print "File %s has been cleared "% filename

line1 = raw_input("Enter your name")
line2 = raw_input("Enter your age")
line3 = raw_input("Enter your weight")

file_handle.write(line1 + "\n" + line2 + "\n" + line3)
file_handle.write("\n")

#ile_handle.write(line2i)
#ile_handle.write("\n")

#ile_handle.write(line3)
#ile_handle.write("\n")

print "Now closing the file"
file_handle.close()

print "File closed succesfully"


