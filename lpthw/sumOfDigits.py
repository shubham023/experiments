#! /usr/bin/python

def sumOfDigits(num):
	orig_num = num 
	total = 0
	while num > 0:	
		total = total + (num % 10)
		num //=  10
	print "Sum of digits for number %d is : %d" % (orig_num, total)
def main():
	number = int (raw_input("Enter a Number : "))
	print "You have enetered %d" % number
	sumOfDigits(number)

main()
