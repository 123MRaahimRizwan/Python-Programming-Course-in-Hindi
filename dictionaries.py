# abyss: a deep hole in the ground 

cities = {"Raahim":"Karachi", "Skillf":"Hyderabad", "Shubh":"Lahore"}

print(type(cities))
print(cities['Shubh'])

cities['Ankit'] = 'Multan'
cities['Iman'] = "Faisalabad"

print(cities)
del cities['Shubh']

print(cities)
print(dir(cities))

cities['Ankit'] = 'Multan'
cities1 = cities.copy()

print(cities1)
print(cities.items())
print(cities.get("Skillf"))
print(cities['Skillf'])
