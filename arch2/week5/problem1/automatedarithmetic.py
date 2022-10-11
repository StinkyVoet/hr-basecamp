import random

"""
A primary school teacher needs to automate basic arithmetic (summation, multiplication table, subtraction) exercises for her students. 
You are asked to implement a program that asks what type of the arithmetic the user needs to practice. 
Then, the program will generate exercises and the user should give the result. Consider the following features for the program:

For each arithmetic operation keep the total number of the exercises 10.

The program must be interactive: for example, if the chosen exercise is multiplication table, 
then the program generates two random numbers (check how python can generate random integers: Week 01: Step 01, Exercise 2, Code 4), 
like 3 and 5; the program prints 3 * 5 = and the user must give the result; the program will print if the answer was correct 
or wrong and then the program will generate next question.

Your program must be implemented with a function `arithmetic_operation(arithmetic_type)`, 
which can create a sum for each arithmetic operation based on the input given by a user (summation, multiplication, subtraction).

Numbers for summation and subtractions will be between 1 and 100.

For other aspects of the program feel free to decide your choice.
- Extented version: Extend your program such that it collects all the mistakes from the user and prints them at the end.
- Extented version: The teacher would like to know which questions are difficult for her students. Extend your program such that it measures the time that the students takes to answer each question. For each question collect the information in a tuple like (question, correct or wrong,time). The program collects all the results in a list and prints them at the end.
- Extented version: Sort the list of the results based on their time before printing it.
"""

def arithmetic_operation(arithmetic_type):
    match arithmetic_type:
        case 'summation': summation()
        case 'multiplication': multiplication()
        case 'subtraction': subtraction()
        case _: print("Invalid input.")

def summation():
    for _ in range(10):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        answer = int(input(f"{num1} + {num2} = "))

        if answer == num1 + num2:
            print("Correct")
        else:
            print("Wrong")

def multiplication():
    for _ in range(10):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        answer = int(input(f"{num1} * {num2} = "))

        if answer == num1 * num2:
            print("Correct")
        else:
            print("Wrong")

def subtraction():
    for _ in range(10):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        answer = int(input(f"{num1} - {num2} = "))

        if answer == num1 - num2:
            print("Correct")
        else:
            print("Wrong")

if __name__ == '__main__':
    input_type = input()
    arithmetic_operation(input_type)