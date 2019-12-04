import random
input_file = open("temps_input.txt", 'w')
out_file = open("temps_output.txt",'w')

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        input_celcius = int(input("Enter number of celcius :"))

        for x in range(input_celcius):
            float_number =(random.uniform(-200,200))
            print((float(float_number),"C"), file=input_file)
            fahrenheit = float_number * 9.0 / 5 + 32
            print(("Result: {:.15f} F".format(fahrenheit)), file=out_file)
    elif choice == "F":
        input_fahrenheit = int(input("Enter number of fahrenheit :"))

        for x in range(input_fahrenheit):
            float_number = (random.uniform(-200, 200))
            print((float(float_number),"F"), file=input_file)
            celsius = 5 / 9 * (float_number - 32)
            print(("Result: {:.15f} C".format(celsius)), file=out_file)

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")