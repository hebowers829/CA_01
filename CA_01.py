# Programmer: Hannah Bowers
# Course: CS151, Dr. Simari
# Date: 1/30/19
# Problem Statement: determine the area of a room and amount of primer and paint in gallons necessary/
# to cover 4 walls and the ceiling
# Input: length, width, and height of a room
# Output: Total area of room and amount of paint and primer needed for room

import math

# Display Purpose

print("This program will tell you how much primer and paint you will need to paint 4 walls and the ceiling of a room")

# ask for length

length = input("Enter the length of the room in feet: ")
length = float(length)

# ask for width

width = input("Enter the width of the room in feet: ")
width = float(width)

# ask for height

height = input("Enter the height of the room in feet: ")
height = float(height)

# calculate area

perimeter = (length + width) * 2

wall_area = perimeter * height

ceiling_area = length * width

total_area = wall_area + ceiling_area

# display area

print"The total area of the room that needs paint is:", total_area, "in sq. feet"

# calculate total gallons of primer

gallons_of_primer = total_area / 200

# display total gallons of primer needed

print"Total number of gallons of primer:", gallons_of_primer

# calculate total gallons of paint

gallons_of_paint = total_area / 350

# display gallons of paint needed

print"Total number of gallons of paint:", gallons_of_paint

# thank user for using program

print("Thank you for using this program, have a nice day.")
