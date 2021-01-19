def outer(num,num2):
    def inner (a,b):
        res = num+num2
        return res
    return inner(1,2)
print(outer(3,4)) 