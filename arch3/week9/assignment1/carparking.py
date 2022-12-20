from datetime import datetime
import math


# ParkedCar class to store information of parked cars.
class ParkedCar:
    license_plate: str
    check_in: datetime

    def __init__(self, license_plate: str, check_in: datetime) -> None:
        self.license_plate = license_plate
        self.check_in = check_in


# Day car parking machine. Max parking fee is 24 hours (hourly_rate * 24).
class CarParkingMachine:
    capacity: int
    hourly_rate: float
    parked_cars: dict[str, ParkedCar]

    def __init__(self, capacity: int, hourly_rate: float = 2.5) -> None:
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}

    def check_in(self, license_plate: str, time: datetime = datetime.now()) -> bool:
        if len(self.parked_cars) >= self.capacity:
            return False

        if license_plate in self.parked_cars:
            return False

        self.parked_cars[license_plate] = ParkedCar(license_plate, time)
        return True

    def check_out(self, license_plate: str) -> float:
        fee = self.get_parking_fee(license_plate)
        self.parked_cars.pop(license_plate)
        return fee

    def get_parking_fee(self, license_plate: str) -> float:
        check_in = self.parked_cars[license_plate].check_in
        diff_datetime = datetime.now() - check_in
        diff_hours = math.ceil(diff_datetime.total_seconds() / 3600)
        diff_hours = 24 if diff_hours > 24 else diff_hours

        return round(diff_hours * self.hourly_rate, 2)


def main():
    # build menu structure as following
    # the input can be case-insensitive (so E and e are valid inputs)
    # [I] Check-in car by license plate
    # [O] Check-out car by license plate
    # [Q] Quit program
    cpm = CarParkingMachine(10)
    while True:
        print(
            "[I] Check-in car by license plate\n"
            "[O] Check-out car by license plate\n"
            "[Q] Quit program"
        )
        match input().upper():
            case "I":
                license_plate = input()
                if cpm.check_in(license_plate, datetime.now()):
                    print("License registered")
                else:
                    print("Capacity reached")
            case "O":
                license_plate = input()
                fee = format(cpm.check_out(license_plate), ".2f")
                print(f"Parking fee: {fee} EUR")
            case "Q":
                quit()
            case _:
                continue


if __name__ == "__main__":
    main()
