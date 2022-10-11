"""
Write a program that determines the name of a shape from its number of sides. 
Read the number of sides from the user and then report the appropriate name as part of a meaningful message. 
Your program should support shapes with anywhere from 3 up to (and including) 10 sides. 
If a number of sides outside of this range is entered then your program should display an appropriate error message.
"""

sides = int(input())

if sides == 3:
    print("Triangle")
elif sides == 4:
    print("Square")
elif sides == 5:
    print("Pentagon")
elif sides == 6:
    print("Hexagon")
elif sides == 7:
    print("Octagon")
elif sides == 8:
    print("Heptagon")
elif sides == 9:
    print("Nonagon")
elif sides == 10:
    print("Decagon")
else:
    print("Unavailable size")
    quit(1)
