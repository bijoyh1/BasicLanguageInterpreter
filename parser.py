#NEWEST
import sys

f = open('output.txt', 'w')
sys.stdout = f

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
variables = {'N': 20000, 'S': 20002}
variablesValue = {20000: '2', 20001: '0', 20002: 'S'}
operators = {'+', '-', '*', '/', '^'}
f = open("code 1 Final.txt",'r')
#g = open("code1error.txt",'w')

#Line Count
lines = f.read().splitlines()
last_line = lines[-1]
totalLines = last_line.split(" ")
totalLines = totalLines[1]
f.close()
f = open("code 1 Final.txt", 'r')

# Errors Explanation
LETERROR = "There is a let error. There is no assignment operator after the word let. The correct syntax for the let " \
           "operator is a let followed by the variable name and then an '=' and the value to be assigned. For " \
           "example 'LET x = 1' "
PRINTERROR = "The variable after PRINT doesn't exist. After the print statement, it should have the variable to be " \
             "printed. "
GOTOERROR = "The GOTO line doesn't exist. The line must be a valid line number."
VARIABLESERROR = "The variable doesn't exist. The variable must first be declared using a LET."
ENDERROR = "There is no end token at the end of the file. The file doesn't have an END at end. It is needed to tell " \
           "the program when to stop running. "

# Error Catching
def checkEndError():
    if len(last_line.split(" "))< 3 or last_line.split(" ")[2] != keytable.get("END"):
        print("Line "+ last_line.split(" ")[1])
        print("Token: 10000")
        print("<block> -> <statement>-> <end_statement> <end_statement> -> END")
        print(last_line.split(" "))
        print(ENDERROR)

def errorCatching(x):
    if x[2] == keytable.get('LET'):
        if x[4] != keytable.get("="):
            print("Line " + x[1])
            print("Token: 10008")
            print("<block> -> <statement> -> <declaring_statement>")
            print(x)
            print(LETERROR)
            return
    elif x[2] == keytable.get('PRINT'):
        if x[3] not in variables.keys():
            print("Line " + x[1])
            print("Token: 10028")
            print("block> -> <statement> -> <print_statement>")
            print("x[3]" + x[3])
            print(len(variables))
            print(PRINTERROR)
    elif x[2] == keytable.get('IF'):
        print("Line " + x[1])
        print("Token: 1001")
        print("<block> -> <statement> -><if_statement>")
        print(x)
        print(PRINTERROR)
        return if_statement(x)

#search dictionary
def get_key_variables(x):
    for key, value in variables.items():
         if x == value:
             return key
def get_key_keytable(x):
    for key, value in keytable.items():
         if x == value:
             return key
def indentify(x):
    if x in keytable.values():
        return get_key_keytable(x)
    elif int(x) in variables.values():
        return str(get_key_variables(int(x)))
    else:
        return x

#Statement Types
def let(x):
    y = x[0:2] + x[3:]
    return " -> <declaring_statement>" + assignment_statement(y)

def print_out(x):
    y = x[0:2] + x[3:]
    return " -> <print_statement>" + statement_type(y)

def rem(x):
    return " -> <comment_statement> -> <literal_String>\n<literal_String> -> " + " ".join(x[3:]) + "\n"

def if_statement(x):
    y =x[0:2] + x[x.index(keytable.get(')'))+1:]
    t =x[0:2] + x[x.index(keytable.get('('))+1:x.index(keytable.get(')'))]
    return " -><if_statement> -> <boolean_expression>" + str(boolean_statement(t)) + str(statement_type(y))

def goto(x):
    y= x[0:2] + x[3:]
    return " -> <goto_statement>" + str(statement_type(y))

def assignment_statement(x):
    y = x[0:2] + x[x.index(keytable.get('='))+1:]
    t = x[0:3]
    return " -> <assignment_statement> -> <Literal_variable> <eq_operator> <arithmetic_expression>\n" + statement_type(t) + "<eq_operator> -> =\n" \
            + str(statement_type(y))


def arithmetic_statement(x):
    operator = ''
    index = 0
    for op in operators:
        if keytable.get(op) in x:
            operator = op
            index = x[x.index(keytable.get(op))]
            break

    y = x[0:x.index(keytable.get(operator))]
    z = x[0:2] + x[x.index(keytable.get(operator)) + 1:]
    return "<arithmetic_statement> -> <arithmetic_statement> <operator> <arithmetic_statement>\n" + str(statement_type(y)) \
           + "<operator> -> " + operator + "\n"\
           + str(statement_type(z))

def literal_variable(x):
    if get_key_variables(int(x[2])) not in variables.keys():
        print("Line " + x[1])
        print("Token not found")
        print("<literal_variable>")
        print(ENDERROR)
        return VARIABLESERROR
    else:
        return "-> <literal_variable>\n<literal_variable> -> " + get_key_variables(int(x[2])) + "\n"

def literal_integer(x):
    return "-> <literal_integer>\n<literal_integer> -> " + x[2] + "\n"

def boolean_statement(x):
    return statement_type(x[0:3]) + " -> <boolean_operator>\n<boolean_operator> -> " + get_key_keytable(x[3]) + "\n" + statement_type(x[0:2] + x[4:])

def end(x):
    return "-> <end_statement>\n<end_statement> -> END\n"

#Finds type of statement
def statement_type(x):
    errorCatching(x)
    if x[2] == keytable.get('END'):
        return end(x)
    elif x[2] == keytable.get('LET'):
        return let(x)
    elif x[2] == keytable.get('REM'):
        return rem(x)
    elif x[2] == keytable.get('PRINT'):
        return print_out(x)
    elif x[2] == keytable.get('IF'):
        return str(if_statement(x))
    elif x[2] == keytable.get('GOTO'):
        if int(x[3]) > int(totalLines):
            print("Line " + x[1])
            print("10009")
            print("<block> -> <statement> -> <goto_statement>")
            print(GOTOERROR)
        return goto(x)
    elif int(x[2]) in variables.values() and len(x) >= 4 and x[3] == keytable.get('='):
        return assignment_statement(x)
    elif keytable.get('+') in x or keytable.get('-') in x or keytable.get('/') in x or keytable.get(
            '*') in x or keytable.get('^') in x:
        return arithmetic_statement(x)
    elif int(x[2]) in variables.values():
        return literal_variable(x)
    elif x[2] not in keytable.values() or x[2] not in variables.values():
        return literal_integer(x)
    return ""

def prefix(x):
    if x[2] == keytable.get('LET'):
        y = indentify(x[4])+ indentify(x[3]) + indentify(x[5])
        return y
    elif x[2] == keytable.get('PRINT'):
        y = indentify(x[3])
        return y
    elif x[2] == keytable.get('IF'):
        y = indentify(x[5]) + indentify(x[4]) + indentify(x[6]) + str(prefix(x[6:]))
        return y
    elif x[2] == keytable.get('GOTO'):
        y = indentify(x[3])
        return y
    elif x[2] == keytable.get('REM'):
        y = "Comment Statement no prefix\n"
        return y
    elif x[2] == keytable.get('END'):
        y = "END Statement no prefix\n"
        return y
    elif int(x[2]) in variables.values():
        if x[3] == keytable.get('='):
            t = x[0:2] + x[4:]
            y = indentify(x[3]) + indentify(x[2]) + str(prefix(t))
            return y
        else:
            y = indentify(x[3]) + indentify(x[2]) + indentify(x[4])
            return y

# Imports variables from scanner
def importDictionary():
    dict = open("variable Dictionary.txt", 'r')
    x = dict.read()
    x = x.replace("{", "")
    x = x.replace("}", "")
    x = x.replace("'", "")
    x = x.replace(":", "")
    x = x.replace(",", "")
    splitX = x.split(" ")
    for y in range(0,len(splitX),2):
        variables[splitX[y]] = int(splitX[y+1])

    dict = open("variable Value Dictionary.txt", 'r')
    x = dict.read()
    x = x.replace("{", "")
    x = x.replace("}", "")
    x = x.replace("'", "")
    x = x.replace(":", "")
    x = x.replace(",", "")
    splitX = x.split(" ")
    for y in range(0, len(splitX), 2):
        variablesValue[splitX[y]] = int(splitX[y + 1])

#Makes the prefix for each line
def create_prefix(x):
    prefix_string = ""
    prefix_string = prefix_string + str(prefix(x))
    print("Prefix for Line " + x[1] + ": ")
    print(prefix_string,end="")
    print()
#Makes the grammer for each line
def create_grammar(x):
    parse_string = "<block> -> <statement>"
    parse_string = parse_string + statement_type(x)
    print("Line: " + x[1])
    print(parse_string,end="")

#Starts the Prefix and Grammer loops.
#import Dictionary()
checkEndError()
for x in f:
    x = x.split(" ")
    create_grammar(x)
    create_prefix(x)
    print()
