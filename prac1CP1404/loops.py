for i in range(1, 21, 2):
    print(i, end=' ')
print()
#a
for x in range (0,101,10):
    print(x, end=' ')
print()
#b
for b in range (20,0,-1):
    print (b, end=' ')
print()
#c
number = int(input("Enter Number:"))
for i in range(number):
    print ("*", end=' ')
#d
print("\n")
num3 = int(input("Enter Number:"))
for c in range(num3):
    for j in range(c+1):
        print("*", end=' ')
    print()
