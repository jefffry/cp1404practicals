import random

CONSTANTS = (1, 45)


def main():
    num_list = []
    quick_picks = int(input("Enter number of quickpicks :"))

    for x in range(1,quick_picks+1):
        for i in range(1,7):

            rand_num = (random.randint(CONSTANTS[0],CONSTANTS[1]))
            while rand_num in num_list:
                rand_num = (random.randint(CONSTANTS[0],CONSTANTS[1]))
            else:
                pass
            num_list.append(rand_num)
            num_list.sort()
        print(num_list)
        num_list = []


main()