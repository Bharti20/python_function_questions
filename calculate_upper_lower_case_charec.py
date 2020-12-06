def string(letters):
    i=0
    count=0
    count2=0
    while i<len(letters):
        if letters[i].isupper():
            count=count+1
        elif letters[i].islower():
            count2=count2+1
        i=i+1
    print("upper case charecters:", count)
    print("lower case charecters:",count2)
string("The quick Brow Fox")