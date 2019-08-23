item_amount = int(input("Please enter number of items "))
sales = 0
while item_amount < 0:
    item_amount = int(input("Invalid items. Please enter number of items "))
for i in range(item_amount):
    price = float(input("Price of item: $"))
    sales += price
if sales > 100:
    sales *= 0.9
print("Total Price for {} items is ${}".format(item_amount, sales))

