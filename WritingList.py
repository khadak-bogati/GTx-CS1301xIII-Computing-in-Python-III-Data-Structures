
myList = ["David", "Lucky", "Vrushali", "Ping" \
		  "Natalie", "Dana", "Addison", "Jasmine"]
outputFile = open("OutputFile.txt", "w")
for name in myList:
	outputFile.write(name + "\n")
outputFile.close()





==================================================================
inputFile = open("OutputFile.txt", "r")

myInt1  = int(inputFile.readline())
myInt2 = int(inputFile.readline())
myInt3 = int(inputFile.readline())

print("myInt1: ", myInt1)
print("myInt2: ", myInt2)
print("myInt3: ", myInt3)
inputFile.close()
