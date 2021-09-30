"""
Created by: Noah Beebe
Date: 9/2/2021
Cover Crop Calculator: use this program to figure out how much of a certain cover crop you
need to cover your field.

"""
# display a welcome message
print("Cover Crop Calculator")
print()

print("Estimated Cover Crop Area")
print()

# get input from the user
field_length = float(input("Enter length of field in terms of feet:\t\t"))
field_width = float(input("Enter width of field in terms of feet:\t\t"))

# calculate total area of field
area = field_length * field_width
area = round(area, 2)

# calculates the amount of acres based off of the users input
acre = area / 43560

# gets input from the user for the seeding rate based off of whatever crop they are going to use
seeding_rate = float(input("Enter seeding rate in terms of pounds:\t\t"))

# calculates the amount of cover crop needed by taking seeding rate times acre
cover_crop = seeding_rate * acre

# format and display the result
print()
print("Estimated Area of Field:\t" + str(area))
print()
print("Estimated Acreage of Field:\t" + str(acre))
print()
print("Estimated amount of cover crop needed:\t" + str(cover_crop))
print()
print("Bye")
