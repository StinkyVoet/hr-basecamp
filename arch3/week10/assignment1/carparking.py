from datetime import datetime
import math


# ParkedCar class to store information of parked cars.
class ParkedCar:
    license_plate: str
    check_in: datetime

    def __init__(self, license_plate: str, check_in: datetime) -> None:
        self.license_plate = license_plate
        self.check_in = check_in


class CarParkingLogger:
    @classmethod
    def log_check_in(cls, id: str, time: datetime, license_plate: str):
        cls.log_action(action="check-in", id=id, time=time, license_plate=license_plate)

    @classmethod
    def log_check_out(cls, id: str, time: datetime, license_plate: str):
        cls.log_action(
            action="check-out", id=id, time=time, license_plate=license_plate
        )

    @staticmethod
    def log_action(action: str, id: str, time: datetime, license_plate: str):
        time_string = time.strftime("%d-%m-%Y %H-%M-%S")

        f = open("carparkinglog.txt", "a")
        f.write(
            f"{time_string};cpm_name={id};license_plate={license_plate};action={action}\n"
        )
        f.close()

    @staticmethod
    def get_machine_fee_by_day(cpm_name: str, date: str) -> float:
        parked_cars = {}
        total_fee = 0
        with open("carparkinglog.txt", "r") as log:
            for entry in log:
                entry_split = entry.split(";")
                entry_date = entry_split[0]
                if entry_split[1] not in cpm_name or date not in entry_date:
                    continue

                match entry_split[-1].replace("\n", ""):
                    case "check-in":
                        parked_cars[entry_split[2]] = ParkedCar(
                            entry_split[2], entry_date
                        )
                    case "check-out":
                        diff_datetime = entry_date - parked_cars[entry_split[2]]
                        diff_hours = math.ceil(diff_datetime.total_seconds() / 3600)
                        diff_hours = 24 if diff_hours > 24 else diff_hours
                        total_fee += round(diff_hours * 2.5, 2)
        return math.ciel(total_fee)

    @staticmethod
    def get_total_car_fee(license_plate: str) -> float:
        parked_cars = {}
        total_fee = 0
        with open("carparkinglog.txt", "r") as log:
            for entry in log:
                entry_split = entry.split(";")

                if entry_split[2] not in license_plate:
                    continue

                match entry_split[-1].replace("\n", ""):
                    case "check-in":
                        parked_cars[license_plate] = ParkedCar(
                            license_plate, entry_split[0]
                        )
                    case "check-out":
                        diff_datetime = entry_split[0] - parked_cars[license_plate]
                        diff_hours = math.ceil(diff_datetime.total_seconds() / 3600)
                        diff_hours = 24 if diff_hours > 24 else diff_hours
                        total_fee += round(diff_hours * 2.5, 2)


# Day car parking machine. Max parking fee is 24 hours (hourly_rate * 24).
class CarParkingMachine:
    id: str
    capacity: int
    hourly_rate: float
    parked_cars: dict[str, ParkedCar]
    logger: CarParkingLogger

    def __init__(self, capacity: int, id: str, hourly_rate: float = 2.5) -> None:
        self.capacity = capacity
        self.id = id
        self.hourly_rate = hourly_rate
        self.parked_cars = {}
        self.logger = CarParkingLogger()

        try:
            with open("carparkinglog.txt", "r") as log:
                for entry in log:
                    vars = {
                        "time": None,
                        "cpm_name": None,
                        "license_plate": None,
                        "action": None,
                    }
                    for variable in entry.split(";"):
                        try:
                            key, value = variable.split("=")
                            vars[key] = value.replace("\n", "")
                        except ValueError:
                            vars["time"] = datetime.strptime(
                                variable, "%d-%m-%Y %H-%M-%S"
                            )

                    if self.id != vars["cpm_name"]:
                        continue

                    if vars["action"] == "check-in":
                        self.parked_cars[vars["license_plate"]] = ParkedCar(
                            vars["license_plate"], vars["time"]
                        )
                    elif vars["action"] == "check-out":
                        self.parked_cars.pop(vars["license_plate"])
        except FileNotFoundError:
            pass

    def check_in(self, license_plate: str, time: datetime = datetime.now()) -> bool:
        if len(self.parked_cars) >= self.capacity:
            return False

        if license_plate in self.parked_cars:
            return False

        self.parked_cars[license_plate] = ParkedCar(license_plate, time)

        self.logger.log_check_in(id=self.id, time=time, license_plate=license_plate)
        return True

    def check_out(
        self,
        license_plate: str,
        check_out_time: datetime = datetime.now(),
    ) -> float:
        fee = self.get_parking_fee(license_plate)
        self.parked_cars.pop(license_plate)
        self.logger.log_check_out(
            id=self.id, time=check_out_time, license_plate=license_plate
        )
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
    cpm = CarParkingMachine(capacity=10, id="North")
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
