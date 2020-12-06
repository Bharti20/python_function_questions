def divisible_number(Limit):
    i=0
    sum=0
    while i<=Limit:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    print(sum)
divisible_number(10)
