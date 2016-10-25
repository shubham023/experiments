#! /usr/bin/python

from sys import argv

filename, user = argv
prompt = ">>>"

print "Hi %r , you have executed %r script"% (user,filename)

print "Now you will have a command prompt asking some details of yours"

age_query = prompt + " What is your age %s "% user

age = int(raw_input(age_query))
age_output = prompt + " Thanks %s, your age is %d years "% (user, age) 


weight_query = prompt + " How much weight you have %s "% user 
weight = int(raw_input(weight_query))
weight_output = prompt + " Thanks %s, your age is %d kgs "% (user, weight) 

print age_output
print weight_output

print prompt + " Good Bye!!! "
