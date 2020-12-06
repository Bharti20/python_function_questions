number1=int(input("enter first number"))
number2=int(input("enter second number"))
def calculator(number1,number2,operation):
    if operation=="add":
        return number1 + number2
    elif operation=="substract":
        return (number1-number2) 
    elif operation=="multiply":
        return (number1*number2)
    else:
        return( number1/number2)
add_result =calculator (number1,number2,"add")
subtract_result=calculator(number1,number2,"substract")
multiply_result=calculator(number1,number2,"multiply")
divide_resul=calculator(number1,number2,"division")
print(add_result)
print(subtract_result)
print(multiply_result)
print(divide_resul)