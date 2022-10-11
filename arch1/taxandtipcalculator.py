has_input = False
while not has_input:
    try:
        cost = float(input())
    except ValueError:
        continue
    has_input = True

tax = cost * .21
tip = cost * .15
total = cost + tax + tip
print(f"Tax: {tax} , Tip: {tip} , Total: {cost}")
