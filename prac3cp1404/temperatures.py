def main():
    num = False
    while not num:
        try:
            celsius = float(input("Celsius: "))
            num = True
            print("Result: {:.2f} F".format(c_f(celsius)))
        except ValueError:
            print("Invalid")
    number = False
    while not number:
        try:
            fahrenheit = float(input("Fahrenheit:"))
            number = True
            print("Result: {:.2f} F".format(c_f(fahrenheit)))
        except ValueError:
            print("Invalid")

def c_f(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def f_c(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

main()