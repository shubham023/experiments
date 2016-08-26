#! /usr/bin/python

formatter = "%r, %r, %r"

print formatter % (1, 2, 3) 
print formatter % ('hello', 'shubham', 'sharma')
print formatter % (True, False, True)
print formatter %(formatter, formatter, formatter)
print formatter %("Hi This","is Shubham", "Sharma")
