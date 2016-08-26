#! /usr/bin/bash

def break_words(userString):
	""" This function breaks the sentences into words """
	words = userString.split()
	return words

def sort_words(words):
	""" This function will sort the words in a string """
	return sorted(words)

def print_first_word(words):
	""" This function will print the first word from the given words """
	word = words.pop(0)
	print word

def print_last_word(words):
	""" This function prints the last word from the given list of words """
	word = words.pop(-1)
	print word

def sort_sentence(userString):
	""" This function will sort the words in the sentence """
	words = break_words(userString)
	return sort_words(words)

def print_first_and_last(userString):
	""" This function will print the first and last word from the sentences """
	words = break_words(userString)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(userString):
	""" This function will sort the sentence and then it will sort the words and then it will print first and last words """
	words = sort_sentence(userString)
	print_first_word(words)
	print_last_word(words)

#print "Printing the string"
#print_first_and_last("Hello! This is Shubham Kumar Sharma")
#print_first_and_last_sorted("Hello! This is Shubham Kumar Sharma")

