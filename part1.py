# grammar = [
#            ["Programm", ("StmtList")],
#            ["StmtList", ("Stmt", "NextStmt")],
#            ["NextStmt", ("StmtList", "EPSLN")],
#            ["Stmt",  ("Assign", "Print")],
#            ["Assign", ("Id", "=", "Expr")],
#            ["Print", ("!", "Id")],
#            ["Expr", ("+", "Expr", "Expr")],
#            ["Expr", ("-", "Expr", "Expr")],
#            ["Expr", ("*", "Expr", "Expr")],
#            ["Expr", ("/", "Expr", "Expr")],
#            ["Expr", ("Id")],
#            ["Expr", ("Const")],
#            ["Id", ("a")],
#            ["Id", ("b")],
#            ["Id", ("c")],
#            ["Const", ("0")],
#            ["Const", ("1")],
#            ["Const", ("2")],
#            ["Const", ("3")],
#            ["Const", ("4")],
#            ["Const", ("5")],
#            ["Const", ("6")],
#            ["Const", ("7")],
#            ["Const", ("8")],
#            ["Const", ("9")],
#            ]

global i
i = 0

def program():
    global i
    stmtList()

def stmtList():
    global i
    stmt()
    nextStmt()

def stmt():
    global i
    try:
        if tokens[i] == "!":
            prints()
        elif tokens[i] == "a" or tokens[i] == "b" or tokens[i] == "c":
            assign()
    except:
        pass


def nextStmt():
    global i
    try:
        if tokens[i] == ";":
            i += 1
            stmtList()
        else:
            return
    except:
        pass

def assign():
    global i
    id_abc()
    # const()
    try:
        if tokens[i] == "=":
            i += 1
            expr()
        else:
            pass
    except:
        pass

def prints():
    global i
    try:
        if tokens[i] == "!":
            i += 1
            id_abc()
        else:
            return
    except:
        pass

def id_abc():
    global i
    # print(i)
    try:
        if tokens[i] == "a" or tokens[i] == "b" or tokens[i] == "c":
            i += 1
        else:
            return
    except:
        pass

def const():
    global i
    try:
        if tokens[i] == "0" or tokens[i] == "1" or tokens[i] == "2" or tokens[i] == "3" or tokens[i] == "4" or tokens[i] == "5" or tokens[i] == "6" or tokens[i] == "7" or tokens[i] == "8" or tokens[i] == "9":
            i += 1
        else:
            return
    except:
        pass

def expr():
    global i
    try:
        if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/":
            i += 1
            expr()
            expr()
        elif tokens[i] == "a" or tokens[i] == "b" or tokens[i] == "c" or tokens[i] == "0" or tokens[i] == "1" or tokens[i] == "2" or tokens[i] == "3" or tokens[i] == "4" or tokens[i] == "5" or tokens[i] == "6" or tokens[i] == "7" or tokens[i] == "8" or tokens[i] == "9":
            i += 1
        else:
            return
    except:
        pass


def tokenize(string):
    return list(string)

def isValid():
    program()
    try:
        if tokens[i] == "." and len(tokens)-1 == i:
            return True
        else:
            return False
    except:
        return False

def interpret(tokens):
    a = b = c = 0
    for i in range(len(tokens)):
        if tokens[i] == '!':
            if tokens[i+1] == 'a':
                return a
            elif tokens[i+1] == 'b':
                return b
            elif tokens[i+1] == 'c':
                return c
        if tokens[i] == '=':
            if tokens[i-1] == 'a':
                a = math(tokens, i+1, a, b, c)
            elif tokens[i-1] == 'b':
                b = math(tokens, i+1, a, b, c)
            elif tokens[i-1] == 'c':
                c = math(tokens, i+1, a, b, c)

def math(toks, index, a, b, c):
    if toks[index].isnumeric():
        return int(toks[index])
    else:
        stack = []
        i = index;
        while toks[i] != ';':
            stack.append(toks[i])
            if len(stack) > 2:
                if stack[len(stack)-1] in 'abc0123456789' and stack[len(stack)-2] in 'abc0123456789' and stack[len(stack)-3] in '+-*/':
                    first = stack.pop()
                    second = stack.pop()
                    op = stack.pop()

                    if first == 'a':
                        first = a
                    elif first == 'b':
                        first = b
                    elif first == 'c':
                        first = c
                    else:
                        first = int(first)

                    if second == 'a':
                        second = a
                    elif second == 'b':
                        second = b
                    elif second == 'c':
                        second = c
                    else:
                        second = int(second)

                    if op == '+':
                        stack.append(str(first+second))
                    elif op == '-':
                        stack.append(str(first-second))
                    elif op == '*':
                        stack.append(str(first*second))
                    elif op == '/':
                        stack.append(str(first/second))
            i+=1
        return int(stack[0])
       
       
        


# print(grammar)

input_str = input("input: ")
# for i in " ":
#     input_str.replace(i, "")
#
# print(input_str)

tokens = tokenize(input_str)
print(tokens)
#print(isValid())
if isValid():
    print(interpret(tokens))
else:
    print('systax error')
