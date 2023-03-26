import math

#ask user to import bond or investment

user_choice = '''
Choose either 'investment' or 'bond' from the menu to proceed.
Investment - to calculate the amount of interest you'll earn on your investment.
Bond:- to calculate the amount you'll have to pay on a home loan.

'''
print(user_choice)


user_input = input("> ")

if user_input == "investment":
    investment_amount = float(input("Please enter the amount you will initially deposit"))
    rate = float(input("Please enter the interest rate"))
    years = float(input("Please enter the number of years you are planning on investing"))

interest = input("Please choose either 'simple' or 'compund' interest")

if interest == "simple":
       #calculate total amount
        total = investment_amount * (1 + ( rate / 100) * years)
        print(" Your total amount will be " + total)

elif interest == "compund":
        total= investment_amount *math.pow((1+ (rate / 100)), years)
        print(" Your final amount with compound interest will be ") + {round(total, 2)}
else: 
        print(" The option you chose is not valid, please choose from the options 'Simple' or 'Compund ")

if user_input == "bond":
    house_value = float(input(" Please enter the value of your house "))
    yearly_interest_rate = float(input(" Please input the the interest rate "))
    repay = int(input(" Please enter the number of months you plan to take to repay the bond "))
#Calculate repayment
    monthly_interest_rate = (yearly_interest_rate / 12) /100
    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate)** (-repay))
    print({round(repayment, 2)})

else:
    print(" The option you have entered in invalid. Please start again and choose Either 'Investment' or 'Bond'")