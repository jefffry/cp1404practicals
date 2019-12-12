def find_oldest_person(name_list,age_list):
    if len(name_list) == 0 or len(age_list) == 0:
        return "One or more lists are empty"
    if len(name_list) != len(age_list):
        return "Lists are not of equal length"
    max_age = -99
    max_index = -1
    for i in range(len(age_list)):
        if age_list[i] > max_age:
            max_index = 1

    if max_index != -1:
        return name_list[max_index]


def example_2():
    print_header("example 2: Updated examples")
    name_to_age = {"Bill":21, "jane":34, "Sven": 56, "Stark": 34}
    name_to_age.update("Sven": 35)
    print(name_to_age)

def main():
    #names = ['Gilbert','John','Marvel','Ky']
    #ages = [1, 39, 14, 27]
    #oldest_person = find_oldest_person(names, ages)
    #print("Oldest person :", oldest_person)
    example_2()

main()