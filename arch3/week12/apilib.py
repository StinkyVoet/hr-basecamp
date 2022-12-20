from dataclasses import dataclass
import requests


class InvalidKeyException(requests.HTTPError):
    """Key is invalid."""


@dataclass
class Api:
    url: str
    key: str

    def getRequestUrl(self, route: str) -> str:
        return f"{self.url}{route}?key={self.key}dawd"

    def get(self, route: str) -> requests.Response:
        response = requests.get(url=self.getRequestUrl(route))
        if not response.ok():
            raise InvalidKeyException()
        print(vars(response))

    def post(self, route: str, data: dict) -> requests.Response:
        response = requests.post(url=self.getRequestUrl(route), data=data)
