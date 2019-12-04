import random
out_file = open("result.txt", 'w')

score = int(input("Enter number of scores :"))
for x in range(score):
    random_number = (random.randint(0,101))
    print(int(random_number))
    if random_number < 0 or random_number> 100:
        print(("Invalid Score"), file =out_file)

    elif random_number >=50 and random_number <=90:
        print(("Passable"), file =out_file)
    elif random_number >90 and random_number <= 100:
        print(("Excellent"), file =out_file)
    else:
        print(("Bad"), file =out_file)
out_file.close()