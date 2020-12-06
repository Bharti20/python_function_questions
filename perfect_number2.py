def perfect(number):
    i=1
    sum=0
    while i<(number):
        if number%i==0:
            sum=sum+i
        i=i+1
    if sum==number:
        print("perfect number hai")
    else:
        print("not perfect")
perfect(6)