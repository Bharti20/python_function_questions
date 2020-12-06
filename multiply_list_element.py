def sum_number(List):
    sum=1
    i=0
    while i<len(List):
        sum=sum*List[i]
        i=i+1
    return sum
print(sum_number([2,4,5,6]))