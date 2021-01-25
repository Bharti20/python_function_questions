def split_function(string):
    split_str = []
    a = ''
    i=0
    while i<len(string):
        if string[i]==' ':
            split_str.append(a)
            a=''
            i=i+1
        else:
            a=a+string[i]
            i=i+1
    split_str.append(a)
    return split_str
print(split_function('i am bharti'))