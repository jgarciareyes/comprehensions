def sum_range (a,b):
    sum = 0
    for x in range (a,b):
        sum += x
    return sum

'''
sum = 0
for x in range (1,10):
    sum += x
print (sum)
'''
result = sum_range(1,10)
print (result)
new_res = sum_range(result, result+10)
print (new_res)