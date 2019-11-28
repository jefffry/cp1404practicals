sum = 0
items = int(input("Number of items:"))
for i in range(items):
    price= float(input("Price of item:"))
    sum = sum + price
if sum >100:
    discount = sum * 0.1
    sum = sum - discount
print("Total price for ",items,"item is : $",round(sum,2))
