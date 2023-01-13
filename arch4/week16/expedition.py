from dataclasses import dataclass
from datetime import datetime

from climber import Climber
from mountain import Mountain


@dataclass
class Expedition:
    id: int
    name: str
    mountain_id: int
    start: str
    date: datetime
    country: str
    duration: int
    success: bool

    def add_climber(self, climber: Climber):
        pass

    def get_climbers(self) -> list[Climber]:
        pass

    def get_mountains(self) -> list[Mountain]:
        pass

    def convert_date(self, to_format: str) -> str:
        return self.date.strftime(to_format)

    def convert_duration(self, to_format: str) -> str:
        return datetime(minute=self.duration).strftime(to_format)

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    # def __repr__(self) -> str:
    #     return "{}({})".format(
    #         type(self).__name__,
    #         ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]),
    #     )
