#!/usr/bin/env python3
#Program takes input of investment amount and share price and gives out the number of share that can be bought
print("\nProgram to calculate number of shares can be bought\n")
while True:
    investment = float(input("\nenter the investment amount\n"))
    price = float(input("\nEnter the share price\n"))
    print("\nTotal number can be bought is ", round(investment/price))
    program = input('\nDo you want to continue? yes/y || no/n:')
    if program.lower().startswith("y"):
      continue
    elif program.lower().startswith("n"):
      exit()