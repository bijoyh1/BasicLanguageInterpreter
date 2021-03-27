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
f = open("code 1 Final.txt",'r')
g = open("code 1 Parsed.txt",'w')

#Statement Types
def let(x):
    return ""

def print_out(x):
    print(x)
    return " -> <Print_statement> ->"


def rem(x):
    return str(" -> <comment_statement> -> <literal_String>")


def if_statement(x):
    y =x[0:2] + x[x.index(keytable.get(')'))+1:]
    return " -> <boolean_expression>"+ str(statement_type(y))


def goto(x):
    return " -> <goto_statement> -> <literal_integer>\n<literal_integer> -> "+ x[3]


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
        return if_statement(x)
    elif x[2] == keytable.get('GOTO'):
        print("GOTO statment")
        return goto(x)
    return ""


def create_grammar(x):
    parse_string = "<block> -> <statement>"
    parse_string = parse_string + statement_type(x)
    print(parse_string)


for x in f:
    x = x.split(" ")
    create_grammar(x)
