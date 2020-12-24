def nested_sum(x):
    def in_sum(y):
        return x+y
    return in_sum(10)
res=(nested_sum(2))
print(res)
