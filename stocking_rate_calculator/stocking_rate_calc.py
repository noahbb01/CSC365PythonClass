"""
Created by: Noah Beebe
Class: CSC365 Scripting Languages
Date: 9/14/2021
Stocking Rate Calculator: use this program to figure out the number of cattle to put in a pasture
"""
# used for the default number of = used to display a nice neat program
LINE_LENGTH = 55

# Prints out the main header of the program
print('Cow-Calf Pair Pasture Stocking Rates')
print("=" * LINE_LENGTH)

# The starting code from the author used to get the program running
while True:
    forage_sample = int(input('Enter the # of forage samples taken (Valid 1-20): '))
    # tells the user to basically enter an amount 1-20 for the number of samples
    if 0 <= forage_sample <= 20:
        break
    else:
        # used to notify the user that the number they entered is bogus
        print('Forage samples must be from 0 through 20. '
              + 'Invalid Value!')

# displays next prompt for dry clipping samples
print()
print('Please enter dry clipping samples in grams: ')
print("=" * LINE_LENGTH)

# calculates the forage samples
total_ounces = 0
for i in range(forage_sample):  # i tried using this 1, forage_sample + 1 but it started at "Sample 2" and went
    i += 1                      # to Sample 6 so i just went back to the old one i used
    samples_ounces = int(input(f"Sample #{i}: "))
    total_ounces = samples_ounces + total_ounces
print()

# the equations used to display the averages of the square feet and forage per acre
square_foot_avg_lbs = float(round((total_ounces / forage_sample) / 453.592, 3))
forage_per_acre = int((square_foot_avg_lbs * 43560))

# prints out the averages with showing the users
print(f"Square foot avg per pound = {square_foot_avg_lbs}")
print(f"Forage per acre per pound = {forage_per_acre}")
print()

# while statement used to get a number 1-100 and all outside numbers are bogus
while True:
    util_rate = int(input('Enter the utilization rate (Valid 1-100): '))
    # prompts the user to enter a number 1-100
    if 0 <= util_rate <= 100:
        break
    else:
        # prints out a return to user letting them know they need a number 1-100
        print('Utilization Rate must be from 0 through 100. '
              + 'Invalid Value!')

# while statement used to get an accurate number of 0 lbs of cow to about 2000 ish pounds
while True:
    animal_unit_month = int(input('Enter the Animal Unit (1 AU = 1000lb) (Valid 1-2000): '))
    if 0 <= animal_unit_month <= 2000:
        break
    else:
        # prints out a return to user letting them know they need a number 1-2000
        print('Animal Unit must be from 0 through 2000. '
              + 'Invalid Value!')

print()
# calculation to get the average number of calf-cow pair ratio needed in the field
stocking_rate = round((forage_per_acre * (util_rate / 100)) / animal_unit_month, 2)
print('Stocking Rate you should put in the field is ' + str(stocking_rate))

print()
# lets the user know program has ended
print('Bye!')
