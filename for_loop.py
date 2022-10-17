monthly_expenses = [1200,1300,1400,1500,1600]
total = monthly_expenses[0] + monthly_expenses[1]
print(total)

total = 0
for i in monthly_expenses:
    total = total + i
print(total)

print(range(10))
for i in range(10):
    print(i)

# monthly_expenses = [1200,1300,1400,1500,1600]

total = 0
for i in range(len(monthly_expenses)):
    expense = monthly_expenses[i]
    print("Month", i+1, "Expense is:", expense)
    # total += expense 
    total = total + expense
print("Total expense:", total)

key_location = 'garage'
locations = ['bedroom', 'garage', 'chair', 'store']
for i in locations:
    if i==key_location:
        print("Key is found at: ", i)
        break
    else:
        print("Key is not found at:", i)

# Print odd numbers b/w 1,10
for i in range(11):
    if i%2==0:
        continue
    print(i)

# 1 iteration i value = 1

i = 0
while i<=10:
    print(i)
    i=i+1
