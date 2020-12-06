def showNumbers(Limit):
    i=0
    while i<=Limit:
        if i%2==0:
            print(i, "Even")
        else:
            print(i, "Odd")
        i=i+1
showNumbers(3)