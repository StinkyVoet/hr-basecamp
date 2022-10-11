import sys

while True:
    try:
        digits = input()
        if len(digits) != 4:
            raise ValueError

        total = 0
        for (key,number) in digits:
            if key != 0:
                sys.stdout("+")

            sys.stdout(f"{int(i)}")
            total += int(i)
        sys.stdout(f"={total}")
    except ValueError:
        print("error")
        continue
    break

