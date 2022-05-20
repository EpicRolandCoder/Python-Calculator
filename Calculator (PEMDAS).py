def addsub(numsent):
    while ("+" in numsent) and ("-" in numsent):
        if numsent.index("-") < numsent.index("+"):
            numsent[numsent.index("-")-1] = float(numsent[numsent.index("-")-1]) - float(numsent[numsent.index("-")+1])
            numsent.pop(numsent.index("-")+1)
            numsent.pop(numsent.index("-"))
        elif numsent.index("+") < numsent.index("-"):
            numsent[numsent.index("+")-1] = float(numsent[numsent.index("+")-1]) + float(numsent[numsent.index("+")+1])
            numsent.pop(numsent.index("+")+1)
            numsent.pop(numsent.index("+"))
    while "+" in numsent:
        numsent[numsent.index("+")-1] = float(numsent[numsent.index("+")-1]) + float(numsent[numsent.index("+")+1])
        numsent.pop(numsent.index("+")+1)
        numsent.pop(numsent.index("+"))
    while "-" in numsent:
        numsent[numsent.index("-")-1] = float(numsent[numsent.index("-")-1]) - float(numsent[numsent.index("-")+1])
        numsent.pop(numsent.index("-")+1)
        numsent.pop(numsent.index("-"))

def multdiv(numsent):
    while ("/" in numsent) and ("*" in numsent):
        if numsent.index("/") < numsent.index("*"):
            numsent[numsent.index("/")-1] = float(numsent[numsent.index("/")-1]) / float(numsent[numsent.index("/")+1])
            numsent.pop(numsent.index("/")+1)
            numsent.pop(numsent.index("/"))
        elif numsent.index("*") < numsent.index("/"):
            numsent[numsent.index("*")-1] = float(numsent[numsent.index("*")-1]) * float(numsent[numsent.index("*")+1])
            numsent.pop(numsent.index("*")+1)
            numsent.pop(numsent.index("*"))
    while "*" in numsent:
        numsent[numsent.index("*")-1] = float(numsent[numsent.index("*")-1]) * float(numsent[numsent.index("*")+1])
        numsent.pop(numsent.index("*")+1)
        numsent.pop(numsent.index("*"))
    while "/" in numsent:
        numsent[numsent.index("/")-1] = float(numsent[numsent.index("/")-1]) / float(numsent[numsent.index("/")+1])
        numsent.pop(numsent.index("/")+1)
        numsent.pop(numsent.index("/"))

def exponent(numsent):
    while "^" in numsent:
        numsent[numsent.index("^")-1] = float(numsent[numsent.index("^")-1]) ** float(numsent[numsent.index("^")+1])
        numsent.pop(numsent.index("^")+1)
        numsent.pop(numsent.index("^"))  

def simplify(numsent):
    exponent(numsent)
    multdiv(numsent)
    addsub(numsent)
    return(numsent[0])

def innerbrackets(numsent, clopen):
    result = []
    numsent.reverse()
    result.append(len(numsent) - (numsent.index("(")+1))
    numsent.reverse()
    for i, value in enumerate(numsent):
        if i > result[0]:
            if value == ")":
                result.append(i)
    if clopen == "open":
        return result[0]
    if clopen == "closed":
        return result[1]

def bracketsplit(numsent):    
    if "(" in numsent:
        bracketslength = innerbrackets(numsent, "closed") - (innerbrackets(numsent, "open")+1)
        numsent[innerbrackets(numsent, "open")+1] = simplify(numsent[(innerbrackets(numsent, "open")+1):(innerbrackets(numsent, "closed"))])
        for foo in range(bracketslength):
            numsent.pop(innerbrackets(numsent, "open")+2)
        numsent.pop(innerbrackets(numsent, "open"))
        bracketsplit(numsent)
    else:
        simplify(numsent)
        print(numsent[0])

def calculate(numsent):
    numsent = numsent.split()
    bracketsplit(numsent)

userinput = input("This calculator accepts PEMDAS operations. Keep spaces between numbers and operators. Enter an equation: ")
calculate(userinput)