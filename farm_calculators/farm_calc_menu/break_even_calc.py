# !/usr/bin/env python3

"""
Created by: Noah Beebe, Bryce Youngquist
Class: CSC365 Scripting Languages
Date: 9/9/2021
Break Even Calculator: use this program to figure out to break even on farming

"""


def break_even_calc():
    # display a welcome message
    print("Break Even Calculator")
    print()

    # get input from the user
    print("Per Acre")
    print('=' * 30)

    # Calculations used from the input of user
    Yield = int(input("Enter Yield (per Acre):\t"))
    Price = float(input("Enter Buying Price ($):\t"))
    Government_Payment = float(input("Enter Government Payment ($): "))
    Variable_Cost = float(input("Enter Variable Costs ($): "))
    overhead_cost = float(input("Enter Overhead Costs ($): "))

    # Calculations used to produce costs and other stuff
    total_revenue = (Yield * Price) + Government_Payment
    total_cost = Variable_Cost + overhead_cost
    earnings = round(total_revenue - total_cost, 3)
    Break_Evan_Cost = round((total_cost - Government_Payment) / Yield, 2)
    per_bushel_profit = round(Price - Break_Evan_Cost, 2)

    # Noah's code for the yield
    print('=' * 30)

    # used to get percentages from the input of user
    yield2 = Yield * .9
    yield3 = Yield * 1.1

    # Next 8 lines of code are used to display the correct calculations
    total_revenue2 = (yield2 * Price) + Government_Payment
    earnings2 = round(total_revenue2 - total_cost, 2)

    total_revenue3 = round((yield3 * Price) + Government_Payment, 2)
    earnings3 = round(total_revenue3 - total_cost, 2)

    Break_Evan_Cost2 = round((total_cost - Government_Payment) / yield2, 2)
    per_bushel_profit2 = round(Price - Break_Evan_Cost2, 2)

    Break_Evan_Cost3 = round((total_cost - Government_Payment) / yield3, 2)
    per_bushel_profit3 = round(Price - Break_Evan_Cost3, 2)

    # Bryce Code for Cost
    print('=' * 30)
    print()
    total_revenue4 = round((Yield * Price) + Government_Payment, 2)
    total_cost = round((Variable_Cost * .9) + (overhead_cost * .9), 2)
    earnings3 = round(total_revenue4 - total_cost, 2)

    total_revenue5 = round(((Yield * Price) + Government_Payment), 2)
    total_cost2 = round((Variable_Cost * 1.1) + (overhead_cost * 1.1), 2)
    earnings4 = round(total_revenue - total_cost2, 2)

    Break_Evan_Cost4 = round((total_cost - Government_Payment) / Yield, 2)
    per_bushel_profit4 = round((Price - Break_Evan_Cost4), 2)
    Break_Evan_Cost5 = round((total_cost2 - Government_Payment) / Yield, 2)
    per_bushel_profit5 = round((Price - Break_Evan_Cost5), 2)

    # code for the formatting that we got from you debby
    # format for the vertical line column header
    print(f'{"":20s}'
          f'{"":15s}'
          f'{"10% Decrease":>15s}'
          f'{"10% Increase":>15s}'
          f'{"10% Decrease":>15s}'
          f'{"10% Increase":>15s}')

    print(f'{"Break Even Calculator      ":20s}'
          f'{"Per Acre":15s}'
          f'{"in Yield":15s}'
          f'{"in Yield":15s}'
          f'{"in Cost":15s}'
          f'{"in Cost":15s}')

    print(f'{"-" * 20:>20s}'
          f'{"-" * 13:>15s}'
          f'{"-" * 13:>15s}'
          f'{"-" * 13:>15s}'
          f'{"-" * 13:>15s}'
          f'{"-" * 13:>15s}')

    print()

    # All the format for the horizontal lines on the left side of the screen
    print(f'{"Yield":20s}'
          f'{Yield:15.2f}'
          f'{Yield:15.2f}'
          f'{Yield:15.2f}'
          f'{Yield:15.2f}'
          f'{Yield:15.2f}')

    print(f'{"Price":20s}'
          f'{Price:15.2f}'
          f'{Price:15.2f}'
          f'{Price:15.2f}'
          f'{Price:15.2f}'
          f'{Price:15.2f}')

    print(f'{"Gov Payment":20s}'
          f'{Government_Payment:15.2f}'
          f'{Government_Payment:15.2f}'
          f'{Government_Payment:15.2f}'
          f'{Government_Payment:15.2f}'
          f'{Government_Payment:15.2f}')

    print(f'{"Total Revenue":20s}'
          f'{total_revenue:15.2f}'
          f'{total_revenue2:15.2f}'
          f'{total_revenue3:15.2f}'
          f'{total_revenue4:15.2f}'
          f'{total_revenue5:15.2f}')

    print()

    print(f'{"Variable Cost":20s}'
          f'{Variable_Cost:15.2f}'
          f'{Variable_Cost:15.2f}'
          f'{Variable_Cost:15.2f}'
          f'{Variable_Cost:15.2f}'
          f'{Variable_Cost:15.2f}')

    print(f'{"Overhead Costs":20s}'
          f'{overhead_cost:15.2f}'
          f'{overhead_cost:15.2f}'
          f'{overhead_cost:15.2f}'
          f'{overhead_cost:15.2f}'
          f'{overhead_cost:15.2f}')

    print(f'{"Total Cost":20s}'
          f'{total_cost:15.2f}'
          f'{total_cost:15.2f}'
          f'{total_cost:15.2f}'
          f'{total_cost:15.2f}'
          f'{total_cost2:15.2f}')

    print(f'{"Earnings":20s}'
          f'{earnings:15.2f}'
          f'{earnings2:15.2f}'
          f'{earnings3:15.2f}'
          f'{earnings4:15.2f}'
          f'{earnings:15.2f}')

    print()

    print(f'{"Break Even Price":20s}'
          f'{Break_Evan_Cost:15.2f}'
          f'{Break_Evan_Cost2:15.2f}'
          f'{Break_Evan_Cost3:15.2f}'
          f'{Break_Evan_Cost4:15.2f}'
          f'{Break_Evan_Cost5:15.2f}')

    print(f'{"Per Bushel Profit":20s}'
          f'{per_bushel_profit:15.2f}'
          f'{per_bushel_profit2:15.2f}'
          f'{per_bushel_profit3:15.2f}'
          f'{per_bushel_profit4:15.2f}'
          f'{per_bushel_profit5:15.2f}')
