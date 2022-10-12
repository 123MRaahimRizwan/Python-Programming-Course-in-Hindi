items = ['tea', 'coffee', 'socks', 'jacket']
print(type(items))

print(items[0])
print(items[-4])
print(len(items))
print('burger' in items)

items.append("burger")
print(items)

items = ['tea', 'coffee', 'socks', 'jacket']
items.insert(2, 'burger')
print(items)

bitcoin = ['etherium', 'dogecoin']
items2 = items + bitcoin
print(items2)
items[2] = 'juice'
items[3] = 'latte'
print(items)
items[2:4] = 'juice'
print(items)
items[2:4] = ['juice']
print(items)
