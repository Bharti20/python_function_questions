def add(num,num2):
    return(num+num2)
def sub (num,num2):
    return num-num2
def multy(num,num2):
    return num*num2
def division(num,num2):
    return num/num2
def calculator(a=int(input()),b=int(input()), operator=input()):
    if operator=='+':
        return (add(a,b))
    elif operator=='-':
        return sub(a,b)
    elif operator=='*':
        return multy(a,b)
    elif operator=='/':
        return division(a,b)
res=calculator()
print(res)