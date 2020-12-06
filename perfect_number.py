def perfect():
    i=1
    while i<30:
        j=1
        sum=0
        while j<i:
            if i%j==0:
                sum=sum+j
            j=j+1
        if i==sum:
            print(sum)
        i = i+1
perfect()


def perfect(number):
    i=1
    sum=0
    while i<(number):
        j=1
        if number%i==0:
            sum=sum+i
        i=i+1
    if sum==number:
        print(sum)
def perfect_list():
    index=1
    while index<30:
        index = index+1
        a=index
        d=perfect(a)
    return d
perfect_list()
print(perfect_list)