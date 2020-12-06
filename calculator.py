def calculator(number_x,number_y,operation):
    if operation=="add":
        return number_x + number_y
    elif operation=="substract":
        print(number_x-number_y) 
    elif operation=="multiply":
        print(number_x*number_y)
    else:
        print( number_x/number_y)
calculator (20,25,"add")
calculator(40,30,"substract")
calculator(10,40,"multiply")
calculator(40,4,"division")
