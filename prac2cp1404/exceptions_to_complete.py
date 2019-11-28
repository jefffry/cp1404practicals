finished = False
result = 0
while not finished:
    try:
        integer= input("Please enter interger:")
        result = int(integer)
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)