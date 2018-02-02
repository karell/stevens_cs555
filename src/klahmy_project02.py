
tags = {'INDI':'0','NAME':'1','SEX':'1','BIRT':'1','DEAT':'1','FAMC':'1','FAMS':'1','FAM':'0','MARR':'1','HUSB':'1','WIFE':'1','CHIL':'1','DIV':'1','DATE':'2','HEAD':'0','TRLR':'0','NOTE':'0'}

inputFileName = "klahmy_project01.txt"
inputFile = open(inputFileName,"r")
outputFile = open('klahmy_project02_output.txt', 'w')


for line in inputFile:
    outputFile.write("--> " + str(line))
    lineSplit = line.split()
    outputFile.write("<-- " + lineSplit[0] + "|")
    if (lineSplit[0] == "0" and len(lineSplit) > 2 and (lineSplit[2] == "INDI" or lineSplit[2] == "FAM")):
        outputFile.write(lineSplit[2] + "|Y|" + lineSplit[1])
    else:
        outputFile.write(lineSplit[1] + "|")
        if (lineSplit[1] in tags):
            if (tags[lineSplit[1]] == lineSplit[0]):
                outputFile.write("Y")
            else:
                outputFile.write("N")
        else:
            outputFile.write("N")
        outputFile.write("|" + ' '.join(lineSplit[2:]))
    outputFile.write("\n")
inputFile.close()
outputFile.close()