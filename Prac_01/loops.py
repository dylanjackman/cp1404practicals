for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()


stars = int(input("Please enter a number to print out that many *'s: "))
for i in range(stars):
    print("*", end=' ')
print()

for i in range(1, stars + 1):
    print("*" * i)
print()
