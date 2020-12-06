number=int(input("enter the number"))
i=0
first_value=0
second_value=1
while i<number:
    if i<=1:
        next=0
    else:
        next= first_value+second_value
        first_value=second_value
        second_value=next
    i=i+1
print(next)
    