def append_function(element):
    List=[1,2,3]
    List=List+[element]
    return List   
def my_function(i):
    res=append_function(i)
    return res
print(my_function(4))