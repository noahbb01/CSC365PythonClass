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
field_length = float(input("Enter length of field:\t\t"))
field_width = float(input("Enter width of field:\t\t"))

# calculate total area of field
area = field_length * field_width
area = round(area, 2)

# format and display the result
print()
print("Estimated Area of Field:\t" + str(area))
print()
print("Bye")
