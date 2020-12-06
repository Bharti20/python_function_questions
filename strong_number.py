Number = int(input(" Please Enter any Number: "))
Sum = 0
x = Number
while(x > 0):
    Factorial = 1
    i = 1
    Reminder = x % 10
    while(i <= Reminder):
        Factorial = Factorial * i
        i = i + 1
    Sum = Sum + Factorial
    x = x // 10    
if (Sum == Number):
    print("strong number hai")
else:
    print("not strong number")