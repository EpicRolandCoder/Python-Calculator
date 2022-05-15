'''numsent = ["2", "+", "8", "/", "2", "*", "4"]

   numsent[numsent.index("/")-1] = int(numsent[numsent.index("/")-1]) / int(numsent[numsent.index("/")+1])
   numsent.pop(numsent.index("/")+1)
   numsent.pop(numsent.index("/"))'''

def addsub(numsent):
    while ("+" in numsent) and ("-" in numsent):
        if numsent.index("-") < numsent.index("+"):
            numsent[numsent.index("-")-1] = int(numsent[numsent.index("-")-1]) - int(numsent[numsent.index("-")+1])
            numsent.pop(numsent.index("-")+1)
            numsent.pop(numsent.index("-"))
        elif numsent.index("+") < numsent.index("-"):
            numsent[numsent.index("+")-1] = int(numsent[numsent.index("+")-1]) + int(numsent[numsent.index("+")+1])
            numsent.pop(numsent.index("+")+1)
            numsent.pop(numsent.index("+"))
    while "+" in numsent:
        numsent[numsent.index("+")-1] = int(numsent[numsent.index("+")-1]) + int(numsent[numsent.index("+")+1])
        numsent.pop(numsent.index("+")+1)
        numsent.pop(numsent.index("+"))
    while "-" in numsent:
        numsent[numsent.index("-")-1] = int(numsent[numsent.index("-")-1]) - int(numsent[numsent.index("-")+1])
        numsent.pop(numsent.index("-")+1)
        numsent.pop(numsent.index("-"))


def multdiv(numsent):
    while ("/" in numsent) and ("*" in numsent):
        if numsent.index("/") < numsent.index("*"):
            numsent[numsent.index("/")-1] = int(numsent[numsent.index("/")-1]) / int(numsent[numsent.index("/")+1])
            numsent.pop(numsent.index("/")+1)
            numsent.pop(numsent.index("/"))
        elif numsent.index("*") < numsent.index("/"):
            numsent[numsent.index("*")-1] = int(numsent[numsent.index("*")-1]) * int(numsent[numsent.index("*")+1])
            numsent.pop(numsent.index("*")+1)
            numsent.pop(numsent.index("*"))
    while "*" in numsent:
        numsent[numsent.index("*")-1] = int(numsent[numsent.index("*")-1]) * int(numsent[numsent.index("*")+1])
        numsent.pop(numsent.index("*")+1)
        numsent.pop(numsent.index("*"))
    while "/" in numsent:
        numsent[numsent.index("/")-1] = int(numsent[numsent.index("/")-1]) / int(numsent[numsent.index("/")+1])
        numsent.pop(numsent.index("/")+1)
        numsent.pop(numsent.index("/"))

def simplify(numsent):
    numsent = numsent.split()
    multdiv(numsent)
    addsub(numsent)
    print(numsent)

userinput = input("Enter an equation. Keep spaces between numbers and operators. The program relies on an equation being entered correctly: ")
simplify(userinput)