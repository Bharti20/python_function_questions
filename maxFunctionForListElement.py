def max_function(b):
    index=0
    a=0
    while index<len(b):
        if b[index] > a:
            a=b[index]
        index=index+1
    return a
print(max_function([20,10,5]))
    