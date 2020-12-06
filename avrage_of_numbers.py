def sum_number():
    i=0
    sum=0
    count=0
    while i<=2:
        number=int(input("enter the number"))
        count=count+1
        sum=sum+number
        i=i+1
    avrage=sum//count
    print("sum of three number","=",sum)
    print("avrage of three number","=",avrage)
sum_number()

        