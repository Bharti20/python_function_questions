def finding_length(List):
    i=0
    List2=[]
    length=0
    while i>=0:
        if List==List2:
            break
        List2.append(List[i])
        length=length+1
        i=i+1
    return length
def my_function(list2):
    a=finding_length(list2)
    return a
print(my_function([1,2,3,4]))