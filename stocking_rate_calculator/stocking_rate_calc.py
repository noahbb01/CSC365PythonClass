"""
Created by: Noah Beebe
Class: CSC365 Scripting Languages
Date: 9/14/2021
Stocking Rate Calculator: use this program to figure out the number of cattle to put in a pasture
"""
LINE_LENGTH = 55

print("Cow-Calf Pair Pasture Stocking Rates")
print("=" * LINE_LENGTH)

# The starting code from the author used to get the program running
while True:
    forage_samp = int(input("Enter the # of forage samples taken (Valid 1-20): "))
    if forage_samp >= 0 and forage_samp <= 20:
        score_total += test_score
        counter += 1
    elif forage_samp == 999:
        break
    else:
        print("Forage samples must be from 0 through 20."
              + "Invalid Value!")
