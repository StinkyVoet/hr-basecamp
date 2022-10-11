"""
In this exercise you will create a program that displays a multiplication table that shows the products 
of all combinations of integers from 1 times 1 up to and including 10 times 10. 
Your multiplication table should include a row of labels across the top of it containing the numbers 1 through 10. 
It should also include labels down the left side consisting of the numbers 1 through 10.
"""

from sys import stdout

print(f"|{'-' * 5}" * 11 + "|")
print(("|%-5s" * 11 + "|") % ("",1,2,3,4,5,6,7,8,9,10))
print(f"|{'-' * 5}" * 11 + "|")

for i in range(1, 11):
    stdout.write("|%-5s" % i)
    for j in range(1, 11):
        stdout.write("|%-5s" % (j * i))
    stdout.write("|\n")
print(f"|{'-' * 5}" * 11 + "|")
