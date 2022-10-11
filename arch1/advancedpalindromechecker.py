"""
There are numerous phrases that are palindromes when spacing is ignored. 
Examples include “go dog”, “flee to me remote elf” and “some men interpret nine memos”, among many others. 
Write a program that it ignores spacing while determining whether or not a string is a palindrome.
"""

inp = input().replace(" ", "")

if inp == inp[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")