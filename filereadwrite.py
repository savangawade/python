with open(r"E:\python\extend.py",'r+') as fvariable:
    filecontent=fvariable.read()
    print(filecontent)
    fvariable.write("\n#extending a list")
    print("complete reading and writing")