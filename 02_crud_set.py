set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print (size)
print ('col' in set_countries)
print ('per' in set_countries)

# add
set_countries.add('per')
print(set_countries)

# update
set_countries.update({'ven', 'arg'})
print (set_countries)

# remove
#set_countries.remove('ven')
set_countries.discard('ven')
print (set_countries)

#clear -- limpia todo el conjunto

