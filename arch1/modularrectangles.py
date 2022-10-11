"""
Write a program that draws “modular rectangles” like the ones below. 
The user specifies the width and height of the rectangle, and the entries start at 0 and increase typewriter fashion from left to right and top to bottom, 
but are all done mod 10. Example: Below are examples of a 3 x 5 rectangular:

0 1 2 3 4
5 6 7 8 9
0 1 2 3 4
"""

from sys import stdout

width = int(input("Width: "))
height = int(input("Height: "))

for i in range(width * height):
    if i % width == 0:
        stdout.write("\n")
    stdout.write(f"{str(i)[-1]} ")
