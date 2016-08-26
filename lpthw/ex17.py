#! /usr/bin/python

from sys import argv
from os.path import exists

script, src, dest = argv

print "Reading the src"
src_handle = open(src)
src_data = src_handle.read()

print " Read %d bytes of data from %s "% (len(src_data), src)

print "Dest file exists ? ", exists(dest)
raw_input("Hit RETURN to continue or else hit CTRL-C")

dest_handle = open(dest,'w')
dest_handle.write(src_data)

dest_handle.close()
src_handle.close()



 
