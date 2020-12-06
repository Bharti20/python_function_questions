def even_number(number1,number2):
    List=[]
    while number1<number2:
        if number1%2==0:
            List.append(number1)
        number1=number1+1
    print(List)
even_number(4,30)