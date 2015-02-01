# Comments
# 
# 
import sys


print("Welcome to the PND RPG")
username = input("Please enter a character name: ")

# loop here
userin = (input("Is " + username + " an acceptable name? [y/n]: ")).lower()

if (userin[0] is 'yes') is True:
	userin[0] = 'y'

if (userin[0] is 'y') is True:
	print("Okay.")
else: 
	print("Too bad.")

print("")
