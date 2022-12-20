from dotenv import load_dotenv

from config import config
from apilib import *


def main():
    load_dotenv(".env")

    api = Api(url="https://api.basecampcrypto.nl/v1/", key=config["KEY"])
    
    team = api.get("team")
    # print(team)


if __name__ == "__main__":
    main()
