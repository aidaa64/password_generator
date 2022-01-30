#!/usr/bin/env python

import random
import string

print("Hello!, Welcome to password generator.")

def generate_pass():
	while True:		
		try:
			length = int(input("Enter the password length: "))
			break		
		except ValueError:
			print("Enter a number!")


	lower_case = string.ascii_lowercase
	upper_case = string.ascii_uppercase
	numbers = string.digits
	symbols = "!@#$%^&_/*"

	character = list(lower_case + upper_case + numbers + symbols)


	random.shuffle(character)
	temp = random.sample(character,length)

	password = "".join(temp)
	print("Your "+str(length)+" digit password is: " + password)
	
generate_pass()
