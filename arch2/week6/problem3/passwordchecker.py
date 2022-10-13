'''
In an application a valid password must be a combination of digits, uppercase and lowercase letters
and only four symbols * @ ! ? .

The length of the password must not be less than 8 characters
and must not be more than 20 characters.
In case the password is not valid, the user can try maximum three times until it is validated.

Implement a Python program that asks the password of the user and checks if it is a valid password.

* Use sets and set operations to solve this problem.
'''

if __name__ == "__main__":
    # a-z
    validator = set(map(chr, range(97, 123)))
    # A-Z
    validator = validator.union(set(map(chr, range(65, 91))))
    # * @ ! ? .
    validator = validator.union({"*", "@", "!", "?", "."})

    input_str = set(input())
    if not input_str.issubset(validator) or len(input_str) not in range(8, 21):
        print("Invalid")
    else:
        print("valid")