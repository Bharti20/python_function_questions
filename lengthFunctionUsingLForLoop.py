def finding_length(data):
    length=0
    for i in data:
       length=length+1
    return length
def my_function(data2):
    a=finding_length(data2)
    return a
print(my_function({1:2, 3:4, 5:6}))