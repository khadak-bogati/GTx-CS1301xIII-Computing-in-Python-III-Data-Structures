myInt1 = 12
myInt2 = 23
myInt3 = 34
#Open OutputFile.txt in write mode
outputFile = open("OutputFile.txt", "w")
outputFile.write(str(myInt1))
outputFile.write(str(myInt2))
outputFile.write(str(myInt3))
outputFile.close()
