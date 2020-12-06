def string(name):
    i=len(name)
    palidrom=""
    while i>0:
        palidrom=palidrom+(name[i-1])
        i=i-1
    if palidrom==name:
        print("palidrom hai")
    else:
        print("not palidrom")
string("baba")