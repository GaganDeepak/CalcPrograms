#!/usr/bin/env python3
#Program to calculate the compound interest for given period and investment amount
import locale
locale.setlocale( locale.LC_ALL, '' )
print("Program to calculate compounding interest\n")
while True:
    investment = int(input("\nenter the investement amount\n"))
    interest = float(input("\nenter the interest rate\n"))
    period = int(input("\nenter the period\n"))
    amount = investment
    rate = 1+(interest/100)
    for i in range(period):
        amount = amount * rate
    print("\nAmount after the period ", locale.currency( round(amount,2), grouping=True ))
    program = input('\nDo you want to continue? yes/y || no/n:')
    if program.lower().startswith("y"):
      continue
    elif program.lower().startswith("n"):
      exit()