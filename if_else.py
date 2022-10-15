number = int(input("Please enter a number: "))
if number > 10:
    print("Number is greater than 10")
else:
    print("Number is less than 10")

# Ternary operator
message = "Number is greater than 10" if number > 10 else "Number is less than 10"
print(message)

canadian = ['Poutine', 'Bannock', 'Butter tarts', 'Caesars']
indian = ['Dosa', 'Chaat', 'Vada pav', 'Dhokla']
pakistani = ['Nihari', 'Karahi', 'Qorma', 'Pani Puri']
bangladeshi = ['Panta Bhat', 'Chorchori', 'Fuchka', 'Bhorta']

dish = input("Enter a dish name: ")
if dish in canadian:
    print(dish," is canadian.")
elif dish in indian:
    print(dish," is indian.")
elif dish in pakistani:
    print(dish," is pakistani.")
elif dish in bangladeshi:
    print(dish," is bangladeshi.")
else:
    print("Based on my little knowledge I don't know the origin of this", dish)
