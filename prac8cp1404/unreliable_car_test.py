from prac8cp1404.unreliable_car import Unreliable_car


def main():
    taxitest1 = Unreliable_car("TESTTAXI", 100, 50)
    taxitest1.drive(100)
    print(taxitest1)
    taxitest1.drive(50)
    print(taxitest1)


if __name__ == '__main__':
    main()
