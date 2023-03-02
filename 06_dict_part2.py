import random
countries = ['col', 'mex', 'bol', 'arg']
popul_v2 = {country: random.randint(1,100) for country in countries}
print (popul_v2)

result = {country: popul for (country, popul) in popul_v2.items() if popul>20}
print (result)

text = 'Hola, soy Juliana'
unique = {c: c.upper() for c in text if c in 'aeiou'}
print (unique)