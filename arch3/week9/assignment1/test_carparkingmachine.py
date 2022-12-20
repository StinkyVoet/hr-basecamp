from carparking import CarParkingMachine
from datetime import datetime, timedelta


# Test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():
    cpm = CarParkingMachine(10)
    assert cpm.check_in("123-123", datetime.now()) is True


# Test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
    cpm = CarParkingMachine(0)
    assert cpm.check_in("123-123", datetime.now()) is False


# Test for checking the correct parking fees
def test_parking_fee():
    cpm = CarParkingMachine(10)
    # Assert that parking time 2h10m, gives correct parking fee
    cpm.check_in("123-123", datetime.now() - timedelta(hours=2, minutes=10))
    assert cpm.get_parking_fee("123-123") == 7.5
    # Assert that parking time 24h, gives correct parking fee
    cpm.check_in("abc-abc", datetime.now() - timedelta(hours=24))
    assert cpm.get_parking_fee("abc-abc") == 60
    # Assert that parking time 30h == 24h max, gives correct parking fee
    cpm.check_in("123-abc", datetime.now() - timedelta(hours=30))
    assert cpm.get_parking_fee("123-abc") == 60


# Test for validating check-out behaviour
def test_check_out():
    license_plate = "123-123"
    cpm = CarParkingMachine(10)
    cpm.check_in(license_plate, datetime.now() - timedelta(hours=4, minutes=5))

    # Assert that {license_plate} is in parked_cars
    assert license_plate in cpm.parked_cars
    # Assert that correct parking fee is provided when
    # checking-out {license_plate}
    assert cpm.check_out(license_plate) == 12.5
    # Assert that {license_plate} is no longer in parked_cars
    assert license_plate not in cpm.parked_cars
