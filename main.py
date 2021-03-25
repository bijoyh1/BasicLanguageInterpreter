#
# Class:       CS 4308 Section 2
# Term:        Spring 2021
# Name:        Bijoy Shah, Mahad Farah, Gordon Barnes
# Instructor:   Deepa Muralidhar
# Project:  Deliverable 1 Scanner - Python
#
f = open('code 1.txt', 'r')
keytable = {
    "END": "10000",
    "FOR": "10001",
    "NEXT": "10002",
    "DATA": "10003",
    "INPUT#": "10004",
    "INPUT": "10005",
    "DIM": "10006",
    "READ": "10007",
    "LET": "10008",
    "GOTO": "10009",
    "RUN": "10010",
    "IF": "10011",
    "RESTORE": "100012",
    "GOSUB": "100013",
    "RETURN": "10014",
    "REM": "10015",
    "STOP": "10016",
    "ON": "10017",
    "WAIT": "10018",
    "LOAD": "10019",
    "SAVE": "10020",
    "VERIFY": "10021",
    "DEF": "10022",
    "POKE": "10023",
    "PRINT#": "10024",
    "PRINT": "10025",
    "CONT": "10026",
    "LIST": "10027",
    "CLR": "10028",
    "CMD": "10029",
    "SYS": "10030",
    "OPEN": "10031",
    "CLOSE": "10032",
    "GET": "10033",
    "NEW": "10034",
    "TAB(": "10035",
    "TO": "10036",
    "FN": "10037",
    "SPC(": "10038",
    "THEN": "10039",
    "NOT": "10040",
    "STEP": "10041",
    "+": "10042",
    "-": "10043",
    "*": "10044",
    "/": "10045",
    "^": "10046",
    "AND": "10047",
    "OR": "10048",
    ">": "10049",
    "=": "10050",
    "<": "10051",
    "SGN": "10052",
    "INT": "10053",
    "ABS": "10054",
    "USR": "10055",
    "FRE": "10056",
    "POS": "10057",
    "SQR": "10058",
    "RND": "10059",
    "LOG": "10060",
    "EXP": "10061",
    "COS": "10062",
    #"SIN": "10063",
    "TAN": "10064",
    "ATN": "10065",
    "PEEK": "10066",
    "LEN": "10067",
    "STR$": "10068",
    "VAL": "10069",
    "ASC": "10070",
    "CHR$": "10071",
    "LEFT$": "10072",
    "RIGHT$": "10073",
    "MID$": "100074",
    "GO": "10075",
    "(": "10076",
    ")": "10077"
}
varCount = 20000
currentLine = 1
variables = {}
variableValues = {}
tokensScanned = {}


# Finds and adds variables to variable dictionaries and adds variable values to variable value dictionary
def Variable(varCount, line):
    line = line.split()
    variables[line[line.index('LET') + 1]] = varCount
    variableValues[varCount] = line[line.index('LET') + 3]


# Inserts spaces to make file easier to read
g = open('code 1Edited.txt', 'w')
list1 = ['(', ')', "-", '+', '=', '==', ':', "'", '"', '/']
for line in f:
    if ':' in line:
        line1 = line[0:line.find(":") - 1] + '\n'
        line2 = line[line.find(":") + 2:]
        g.write(" " + line1)
        g.write(" " + line2)
    else:
        temp = line
        for char in temp:
            if char in list1:
                temp = temp.replace(char, " " + char + " ")
                temp = temp.replace("  ", " ")
        g.write(" " + temp)
f.close()
g.close()

# Converts all keywords to numbers
f = open('code 1Edited.txt', 'r')
h = open('code 1 Final.txt', 'w')
for line in f:
    temp = line
    for word in temp.split():
        if word == 'LET':
            Variable(varCount, line)
            varCount += 1
        if word in keytable:
            temp = temp.replace(word, keytable[word])
            tokensScanned[word] = keytable[word]
        elif word in variables:
            temp = temp.replace(" " + word, " " + str(variables[word]))
    h.write(temp)
    currentLine += 1
print(variables)
print(variableValues)
print(tokensScanned)
g.close()
