# !/usr/bin/env python3

# display a welcome message
print("Break Even Calculator")
print()

# get input from the user
print("Per Acre")
print('=' * 30)
Yield = int(input("Enter Yield (per Acre):\t"))
Price = float(input("Enter Buying Price ($):\t"))
Government_Payment = float(input("Enter Government Payment ($): "))
Variable_Cost = float(input("Enter Variable Costs ($): "))
overhead_cost = float(input("Enter Overhead Costs ($): "))

total_revenue = (Yield * Price) + Government_Payment
total_cost = Variable_Cost + overhead_cost
earnings = round(total_revenue - total_cost, 3)
Break_Evan_Cost = round((total_cost - Government_Payment) / Yield, 2)
per_bushel_profit = round(Price - Break_Evan_Cost, 2)

# format and display the result
print('=' * 30)
print()
print("Total Cost: " + str(total_cost))
print("Total Revenue: " + str(total_revenue))
print("Total Earnings: " + str(earnings))
print("Costs to Break Even: " + str(Break_Evan_Cost))
print("Per Bushel Profit: " + str(per_bushel_profit))
print()

# Noah's code for the yield
print('=' * 30)
yield2 = Yield * .9
yield3 = Yield * 1.1

total_revenue2 = (yield2 * Price) + Government_Payment
earnings2 = round(total_revenue2 - total_cost, 2)

total_revenue3 = round((yield3 * Price) + Government_Payment, 2)
earnings3 = round(total_revenue3 - total_cost, 2)

Break_Evan_Cost2 = round((total_cost - Government_Payment) / yield2, 2)
per_bushel_profit2 = round(Price - Break_Evan_Cost2, 2)

Break_Evan_Cost3 = round((total_cost - Government_Payment) / yield3, 2)
per_bushel_profit3 = round(Price - Break_Evan_Cost3, 2)

print("Total Revenue with 10% decrease: " + str(total_revenue2))
print("Total Earnings with 10% decrease: " + str(earnings2))
print()
print("Total Revenue with 10% increase: " + str(total_revenue3))
print("Total Earnings with 10% increase: " + str(earnings3))
print()
print("Costs to Break Even: " + str(Break_Evan_Cost2))
print("Per Bushel Profit: " + str(per_bushel_profit2))
print()
print("Costs to Break Even: " + str(Break_Evan_Cost3))
print("Per Bushel Profit: " + str(per_bushel_profit3))

# Bryce Code for Cost165
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

print("Total Cost with 10% decrease: " + str(total_revenue4))
print("Total Cost with 10% decrease: " + str(earnings3))
print()
print("Total Cost with 10% increase: " + str(total_revenue5))
print("Total Cost with 10% increase: " + str(earnings4))
print()
print("Costs to Break Even: " + str(Break_Evan_Cost4))
print("Per Bushel Profit: " + str(per_bushel_profit4))
print()
print("Costs to Break Even: " + str(Break_Evan_Cost5))
print("Per Bushel Profit: " + str(per_bushel_profit5))

print(f'{"":20s}'
      f'{"":15s}'
      f'{"10% Decrease":>15s}'
      f'{"10% Increase":>15s}'
      f'{"10% Decrease":>15s}'
      f'{"10% Increase":>15s}')

print(f'{"BreakEven Calculator":20s}'
      f'{"Per Acre":.15s}'
      f'{"in Yield":.15s}'
      f'{"in Yield":.15s}'
      f'{"in Cost":.15s}'
      f'{"in Cost":.15s}')

print(f'{"-" * 20:>20s}'
      f'{"-" * 13:>15s}'
      f'{"-" * 13:>15s}'
      f'{"-" * 13:>15s}'
      f'{"-" * 13:>15s}'
      f'{"-" * 13:>15s}')

print(f'{"Per Bushel Profit":20s}'
      f'{per_bushel_profit:15,2f}'
      f'{per_bushel_profit2:15,2f}'
      f'{per_bushel_profit3:15,2f}'
      f'{per_bushel_profit4:15,2f}'
      f'{per_bushel_profit5:15,2f}')
