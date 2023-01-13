from dataclasses import dataclass
from datetime import datetime
from dateutil.relativedelta import relativedelta


@dataclass
class Climber:
    id: int
    first_name: str
    last_name: str
    nationality: str
    date_of_birth: datetime

    def get_age(self) -> int:
        return relativedelta(datetime.now(), self.date_of_birth).years

    def get_expeditions(self) -> list["Expedition"]:
        pass

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    # def __repr__(self) -> str:
    #     return "{}({})".format(
    #         type(self).__name__,
    #         ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]),
    #     )
