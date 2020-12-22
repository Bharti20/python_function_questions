def odd(num):
    return "odd hai"
def even(num):
    return "even hai"
def oddEven(a=int(input("user input:-"))):
    if a%2==0:
        return even(a)
    else:
        return odd(a)
print(oddEven())