#Bugs: does not check to make sure that only numbers and operators are in the entered expression

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
        return(numsent)

def calculate():
    numsent = input("Enter Expression: ")
    try:
        numsent = numsent.split()
        bracketsplit(numsent)
        print("Your expression simplifies to: " + str(numsent[0]))
    except:
        numsent ="An error occured. Please enter 'continue' if you wish to try again. Enter anything else to exit: "
        if numsent == 'continue':
            calculate()
        else:
            print('Made by EpicRolandCoder')
            exit()
    if input("Please enter 'continue' if you wish to keep using the calculator. Enter anything else to exit: ") == 'continue':
        calculate()
    else:
        print('Made by EpicRolandCoder')
        exit()

print("This 'calculator' simplifies expressions with NUMBERS and PEMDAS OPERATIONS. Please keep spaces between numbers and operators when entering your expression")

calculate()