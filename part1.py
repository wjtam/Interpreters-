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

# def interpret(tokens):
#     pass

# print(grammar)

input_str = input()
# for i in " ":
#     input_str.replace(i, "")
#
# print(input_str)

tokens = tokenize(input_str)
print(tokens)
print(isValid())
