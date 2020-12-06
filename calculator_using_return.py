def calculator(number_x,number_y,operation):
    if operation=="add":
        return number_x + number_y
    elif operation=="substract":
        return (number_x-number_y) 
    elif operation=="multiply":
        return (number_x*number_y)
    else:
        return( number_x/number_y)
number_1=calculator (20,25,"add")
print(number_1)
number_2=calculator(40,30,"substract")
print(number_2)
number_3=calculator(10,40,"multiply")
print(number_3)
number_4=calculator(40,4,"division")
print(number_4)