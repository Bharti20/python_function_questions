def calculator(number1,number2,operation):
    if operation=="add":
        return number1 + number2
    elif operation=="substract":
        return (number1-number2) 
    elif operation=="multiply":
        return (number1*number2)
    else:
        return( number1/number2)

    
def List_change(List1,List2):
    i=0
    new_list=[]
    while i<1:
        j=0
        while j<len(List1):
            a=calculator(List1[j],List2[j],"multiply")
            new_list.append(a)
            j=j+1
        i=i+1
    return new_list
        
result = List_change([5, 10, 50, 20], [2, 20, 3, 5])

print(result)