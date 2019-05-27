
def income(yearlyInvest, Account, target, workIncome):
    test = True
    years = 0
    while test:
        yearlyIncome = Account * .07
        # print(yearlyIncome)
        Account += yearlyInvest
        workIncome += workIncome*.03
        years += 1

        if years <= 10 & years >= 5:
            yearlyInvest += 500 + (500 * (years * 0.5))
        elif years > 10:
            if yearlyInvest <= (workIncome*.3):
                yearlyInvest += 1000 + (500 * (years * 0.5))
        print("Year:   Investment:  Income from market:")
        print(years, "     ", yearlyInvest, "        ", yearlyIncome, "\n")

        if yearlyIncome >= target:
            print("\n\nIt  will take",  years, " years with", Account, "in the market to make",  yearlyIncome, " passively!")
            break


print("\n\nThis program is to show people entering the workforce how much they should invest into the stock market...")

investment = int(input("How much can you invest per year as of today?"))
account = int(input("How much do you have in the stock market today?"))
career = int(input("What is your careers average income?"))
target = int(input("How much are you looking to make passively"))



income(investment, account, target, career)
