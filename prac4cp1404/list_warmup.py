numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)
#numbers[0] : 3
#numbers[-1] : 2
#numbers[3] : 1
#numbers[:-1] : 3, 1, 4, 1, 5, 9
#numbers[3:4] : 1
#5 in numbers : True
#7 in numbers : False
#"3" in numbers : False
#numbers + [6, 5, 3] : 3, 1, 4, 1, 5, 9, 2, 6, 5, 3


updated_list = [3, 1, 4, 1, 5, 9, 2]
#Change the first element of numbers to "ten"
updated_list[0] = "ten"
#Change the last element of numbers to 1
updated_list[-1] = 1
#Get all the elements from numbers except the first two
print(updated_list[2:])
#Check if 9 is an element of numbers
check = 9 in updated_list
print(check)
#Updated list
print(updated_list)