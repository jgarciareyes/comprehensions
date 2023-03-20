items = [{'product': 'chemise', 'price': 150,},
         {'product': 'pantalon', 'price': 200},
         {'product': 'chaussures', 'price': 90}]

prices = list(map(lambda item: item['price'], items))
print (prices)

def add_taxes (item):
    item ['taxes'] = item['price']*.19
    return item

new_items = list(map(add_taxes, items))
print (new_items)