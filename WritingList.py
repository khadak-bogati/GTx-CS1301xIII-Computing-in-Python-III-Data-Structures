
myList = ["David", "Lucky", "Vrushali", "Ping" \
		  "Natalie", "Dana", "Addison", "Jasmine"]
outputFile = open("OutputFile.txt", "w")
for name in myList:
	outputFile.write(name + "\n")
outputFile.close()
