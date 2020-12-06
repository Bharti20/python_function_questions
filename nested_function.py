def outer_function(num1,num2):
    def inner_function(num1,num2):
        return num1+num2
    add=inner_function(num1,num2)
    return add+5
res=outer_function(10,5)
print(res)