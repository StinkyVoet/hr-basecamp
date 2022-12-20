def report_parked_cars() -> str:
    output = "license_plate;check-in;check-out;parking_fee"
    return output


def report_total_parking_fee():
    output = 0
    return


def main():
    while True:
        print(
            "[P] report all parked cars\n"
            "[F] Report total collected parking fee\n"
            "[Q] Quit program"
        )
        match input().upper():
            case "P":
                pass
            case "F":
                pass
            case "Q":
                quit()
            case _:
                continue

if __name__ == "__main__":
    main()
