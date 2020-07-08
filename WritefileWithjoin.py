myInt1 = 12
myInt2 = 23
myInt3 = 34
myList = ["David", "Lucky", "Vrushali", "Ping" \
		  "Natalie", "Dana", "Addison", "Jasmine"]
outputFile = open("OutputFile.txt", "w")
outputFile.write(str(myInt1) + "\n")
outputFile.write(str(myInt2) + "\n")
outputFile.write(str(myInt3) + "\n")
outputFile.write("\n" .join(myList))
outputFile.close()
