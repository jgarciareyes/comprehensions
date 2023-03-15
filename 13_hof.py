def increment (x):
    return x+5

increment_v2 = lambda x: x+1

def high_of (x, func):
    return x + func(x)

high_of_v2 = lambda x, func: x + func(x)

result = high_of(2, increment)
print (result)

result_v2 = high_of_v2(2, increment_v2)
print (result_v2)

result_v3 = high_of_v2(2, lambda x: x+2)
print (result_v3)

result_v4 = high_of_v2(2, lambda x: x*3)
print (result_v4)