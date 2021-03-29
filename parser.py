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
variables = {
    'MAX': 20000,
    'X': 20001,
    'Y': 20002
}
f = open("code 1 Final.txt",'r')
g = open("code 1 Parsed.txt",'w')

def get_key_variables(x):
    for key, value in variables.items():
         if x == value:
             return key
def get_key_keytable(x):
    for key, value in keytable.items():
         if x == value:
             return key
#Statement Types
def let(x):
    y = x[0:2] + x[3:]
    return " -> <declaring_statement>" + assignment_statement(y)

def print_out(x):
    y = x[0:2] + x[3:]
    return " -> <print_statement>" + statement_type(y)

def rem(x):
    return " -> <comment_statement> -> <literal_String>\n<literal_String> -> " + " ".join(x[3:])

def if_statement(x):
    y =x[0:2] + x[x.index(keytable.get(')'))+1:]
    t =x[0:2] + x[x.index(keytable.get('('))+1:x.index(keytable.get(')'))]
    return " -> <boolean_expression>" + str(boolean_statement(t)) + str(statement_type(y))

def goto(x):
    y= x[0:2] + x[3:]
    return " -> <goto_statement>" + str(statement_type(y))

def arithmetic_statement(x):
    return ""

def literal_variable(x):
    return "-> <literal_variable>\n<literal_variable> -> " + get_key_variables(int(x[2])) + "\n"

def literal_integer(x):
    return "-> <literal_integer>\n<literal_integer> -> " + x[2]+ "\n"

def boolean_statement(x):
    return statement_type(x[0:3]) + " -> <boolean_operator>\n<boolean_operator> -> " + get_key_keytable(x[3]) + "\n" + statement_type(x[0:2] + x[4:])
#Expression Types



#Finds type of statement
def statement_type(x):
    if x[2] == keytable.get('LET'):
        print("LET statment")
        return let(x)
    elif x[2] == keytable.get('REM'):
        print("REM statment")
        return rem(x)
    elif x[2] == keytable.get('PRINT'):
        print("PRINT statment")
        return print_out(x)
    elif x[2] == keytable.get('IF'):
        print("IF statment")
        return str(if_statement(x))
    elif x[2] == keytable.get('GOTO'):
        print("GOTO statment")
        return goto(x)
    # elif ADD CODE HERE:
    #     print("arithmetic statement")
    #     return arithmetic_statement(x)
    elif int(x[2]) in variables.values():
        print("literal Variable")
        return literal_variable(x)
    elif x[2] not in keytable.keys() or x[2] not in variables.values():
        print("literal Integer")
        return literal_integer(x)
    return ""

def create_grammar(x):
    parse_string = "<block> -> <statement>"
    parse_string = parse_string + statement_type(x)
    print("Line: " + x[1])
    print(parse_string,end="")

for x in f:
    x = x.split(" ")
    create_grammar(x)
