code = [
    ["assignment", "N = 3"],
    ["assignment", "S = 0"],
    ["assignment", "S = 0"],
    ["arithmetic", "S = S + N"],
    ["Print", "N"],
    ["Print", "S"],
    ["assignment", "B = 0"],
    ["arithmetic", "B = S - INT ( N / 2 ) * 2"],
    ["Print", "B"],
]

variables = {'N': 20000, 'S': 20001, 'B': 20002}
variablesValue = {20000: '', 20001: '', 20002: ''}

def execute(code):
    print("Program Code:")
    for line in code:
        print(line[0] + ", " + line[1])
    print("")

    print("Runtime Results: ")
    for line in code:
        if line[0] == "assignment":
            assignment(line[1])
        elif line[0] == "arithmetic":
            arithmetic(line[1])
        elif line[0] == "Print":
            Print(line[1])

def assignment(line):
    line = line.split();
    variablesValue[variables.get(line[0])] = line[2]

def arithmetic(line):
    line = line.split();
    math = line[2:]
    i = 2
    for x in math:
        if x in variables:
            line[i]= variablesValue.get(variables.get(x))
        i = i + 1
    newline = calculate(line)
    variablesValue[variables.get(newline[0])] = newline[2]

def calculate(line):
    if "(" in line:
        start = line.index('(')
        end = line.index(')') + 1
        temp = line[start+1:end -1]
        calculate(temp)
        newlist = line[0:start] + line[end:]
        newlist.insert(start,calculate(temp))
        if (len(newlist) == 1):
            return newlist[0]
        else:
            return calculate(newlist)
    elif "INT" in line:
        start = line.index('INT')
        end = line.index('INT') + 2
        temp = line[start:end]
        temp = int(temp[1])
        newlist = line[0:start] + line[end:]
        newlist.insert(start, temp)
        if (len(newlist) == 1):
            return newlist[0]
        else:
            return calculate(newlist)
    elif "*" in line:
        start = line.index('*') - 1
        end = line.index('*') + 2
        temp = line[start:end]
        temp = temp[0] * temp[2]
        newlist = line[0:start] + line[end:]
        newlist.insert(start, temp)
        if (len(newlist) == 1):
            return newlist[0]
        else:
            return calculate(newlist)
    elif "/" in line:
        start = line.index('/') - 1
        end = line.index('/') + 2
        temp = line[start:end]
        temp = int(temp[0]) / int(temp[2])
        newlist = line[0:start] + line[end:]
        newlist.insert(start, temp)
        if(len(newlist) == 1):
            return newlist[0]
        else:
            return calculate(newlist)

    elif "+" in line:
        start = line.index('+') - 1
        end = line.index('+') + 2
        temp = line[start:end]
        temp = int(temp[0]) + int(temp[2])
        newlist = line[0:start] + line[end:]
        newlist.insert(start, temp)
        if (len(newlist) == 1):
            return newlist[0]
        else:
            return calculate(newlist)
    elif "-" in line:
        start = line.index('-') - 1
        end = line.index('-') + 2
        temp = line[start:end]
        temp = int(temp[0]) - int(temp[2])
        newlist = line[0:start] + line[end:]
        newlist.insert(start, temp)
        if (len(newlist) == 1):
            return newlist[0]
        else:
            return calculate(newlist)
    else:
        return line

def Print(line):
    print(variablesValue.get(variables.get(line)))

execute(code)
