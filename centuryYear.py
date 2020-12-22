def calulation(year):
     return year//100
def calculation2(year):
    return year//100+1
def centuryFromYear(year=int(input())):
    if year>=100 and year%100==0:
        return calulation(year)
    elif year>100: 
        return calculation2(year)
    else:
        return("not valid year")
print(centuryFromYear())
        