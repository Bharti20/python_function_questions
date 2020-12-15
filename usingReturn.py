def my_function():
    dic={}
    i=0
    while i<2:
        student=input("enter the name")
        marks=int(input("enter the marks"))
        dic[student]=marks
        i=i+1
    return dic
print(my_function())


# List=[]
# List2=[]
# i=0
# while i<2:
#     student=input("enter the number")
#     List.append(student)
#     marks=int(input("enter the number"))
#     List2.append(marks)
#     i=i+1
# ziplist=zip(List, List2)
# dictionary=dict(ziplist)
# print(dictionary)
    