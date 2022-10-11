print("Convert years to months and days")

has_input = False
while not has_input:
    try:
        years = int(input("Enter an amount of years: "))
    except ValueError:
        print("Not a number")
        continue
    break

print(f"Months: {years*12}")
print(f"Days: {years*365}")
