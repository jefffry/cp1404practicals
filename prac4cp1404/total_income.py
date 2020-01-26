


def income_report(duration, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, duration + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:<5.2f} Total: ${:.2f}".format(month, income, total))


def main():
    incomes = []
    duration = int(input("How many months? "))

    for month in range(1, duration + 1):
        income = float(input("Enter income for month {} : ".format(month)))
        incomes.append(income)

    income_report(duration, incomes)

main()