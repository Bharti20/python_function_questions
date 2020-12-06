def factorial_number(number):
    i=1
    factorial=1
    while i<=number:
        factorial=factorial*i
        i=i+1
    return factorial 
print(factorial_number(6))