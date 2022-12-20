from sense_hat import SenseHat
import requests
import time
import random

sense = SenseHat()
sense.clear(0, 0, 0)

node = 14
key = "4QDBgBIcref8Z5zkPkZj9g"
postUrl = f"https://api.basecampserver.tech/sensors?key={key}"
getUrl = f"https://api.basecampserver.tech/sensors?node_id={node}"

sensor_data = {
    "node_id": node,
    "timestamp": "",
    "temperature": "",
    "humidity": "",
    "pressure": "",
}


def uploadData():
    requests.post(url=postUrl, json=sensor_data)

    print("Upload data to server")

    return


def getData():
    r = requests.get(url=getUrl)
    data = r.json()

    print("got data from server")
    print(data)

    return


def main():
    while True:
        sensor_data["timestamp"] = round(int(time.time()), 2)
        sensor_data["temperature"] = sense.get_temperature()
        sensor_data["humidity"] = sense.get_humidity()
        sensor_data["pressure"] = sense.get_pressure()

        uploadData()
        sense.clear(0, 0, 0)
        getData()

        for i in range(100):
            rand1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            rand2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            picture = [
                rand1, rand2, rand1, rand2, rand1, rand2, rand1, rand2,
                rand2, rand1, rand2, rand1, rand2, rand1, rand2, rand1,
                rand1, rand2, rand1, rand2, rand1, rand2, rand1, rand2,
                rand2, rand1, rand2, rand1, rand2, rand1, rand2, rand1,
                rand1, rand2, rand1, rand2, rand1, rand2, rand1, rand2,
                rand2, rand1, rand2, rand1, rand2, rand1, rand2, rand1,
                rand1, rand2, rand1, rand2, rand1, rand2, rand1, rand2,
                rand2, rand1, rand2, rand1, rand2, rand1, rand2, rand1
            ]

            sense.set_pixels(picture)
            sense.low_light = True
            time.sleep(1)


if __name__ == "__main__":
    main()
