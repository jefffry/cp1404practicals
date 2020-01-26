from prac8cp1404.taxi import Taxi


def main():
    prius1 = Taxi("Prius 1", 100)
    prius1.drive(40)
    print(prius1)
    print("current fare:", prius1.get_fare())
    prius1.start_fare()
    prius1.drive(100)
    print(prius1)
    print("current fare", prius1.get_fare())


if __name__ == '__main__':
    main()
