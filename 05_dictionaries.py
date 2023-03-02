dic = {}
for i in range (1,5):
    dic[i]=i*2
print (dic)

dic_v2 = {i:i*2 for i in range (1,5)}
print (dic_v2)

import random

countries =['col', 'bol', 'per', 'arg']
popul={}
for country in countries:
    popul[country]=random.randint(1,100)

print (popul)

popul_v2 = {country: random.randint(1,100) for country in countries}
print (popul_v2)

names = ['Juli', 'Zucoo', 'Itachi']
ages = [25,36,41]
resultado_esperado={
    'Juli': 25,
    'Zucco': 36,
    'Itachi':41
}

print (list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print (new_dict)
new_dict_v2 = dict(zip(names, ages))
print (new_dict_v2)
