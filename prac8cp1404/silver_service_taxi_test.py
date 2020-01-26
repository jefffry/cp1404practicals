from prac8cp1404.silver_service_taxi import SilverServiceTaxi


def main():
    testcar = SilverServiceTaxi("cartype2", 100, 2)
    testcar.drive(18)
    print(testcar)
    print("the fare is:", testcar.get_fare())


if __name__ == '__main__':
    main()
