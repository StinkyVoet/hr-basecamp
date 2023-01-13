from climber import Climber
from expedition import Expedition
from mountain import Mountain

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


# Test to check if the age of a climber is correct based on the date_of_birth
def test_age_of_climber():
    date_of_birth = datetime.now() - relativedelta(years=30)
    climber = Climber(1, "test", "climber", "nl", date_of_birth)
    
    assert climber.get_age() == 30


# Test to check if the amount of expeditions for a specific climber is returned correctly
def test_amount_of_expeditions_of_climber():
    pass


# Test to check the difference in height and prommence of a mountain
def test_height_difference_mountain():
    pass


# Test to check if the amount of expeditions for a specific mountain is returned correctly
def test_amount_of_expeditions_of_mountain():
    pass


# Test to check if the returned date matches the specified format for that expedition date
def test_expedition_date_conversion():
    pass


# Test to check if the duration is converted from 1H19 to the specified format
def test_expedition_duration_conversion():
    pass


# Test to check the amount of climbers on a specified expedition
def test_amount_of_climbers_on_expedition():
    pass


# Test to validate if the given mountain of a specified expedition is correct
def test_mountain_on_expedition():
    pass
