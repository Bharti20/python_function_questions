def add (a,b):
    print(a+b)
def sub(a,b):
    return(a-b)
def add_sub(a,b,c):
    if c=='+':
        s=add(a,b)
    else:
        s=sub(a,b)
    return s
print(add_sub(8,2,"-"))
