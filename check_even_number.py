def add_number(List1,List2):
    i=0
    while i<1:
        j=0
        while j<len(List1):
            if List1[j]%2==0 and List2[j]%2==0:
                print("dono even hai")
            else:
                print("dono even nahi hai")
            j=j+1
        i=i+1
add_number([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])