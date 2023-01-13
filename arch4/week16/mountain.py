from dataclasses import dataclass


@dataclass
class Mountain:
    id: int
    name: str
    country: str
    rank: int
    height: int
    prominence: int
    range: str

    def height_difference(self) -> int:
        return self.height - self.prominence

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
