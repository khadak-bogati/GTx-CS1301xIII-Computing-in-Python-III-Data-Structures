import string
#Return True if inString contains all digits
def isdigit(inString):
	#Check each character one-by-one
	for character in inString:
		#Check if the character is a digit
		if not character in string.digits:
			#Return false if not 
			return false
	#Return true if we reached here
	return True
myString = "52672"
print(myString.isdigit())
print(myString.isdigit())

