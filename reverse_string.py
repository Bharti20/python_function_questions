def str_function(List):
    i=len(List)
    reverse=""
    while i>0:
        reverse=reverse+List[i-1]
        i=i-1
    print(reverse)
str_function("Bharti")