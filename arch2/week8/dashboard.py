from flask import Flask, render_template
import requests
from datetime import datetime
from statistics import stdev

app = Flask(__name__)

id = 14
getUrl = f"https://api.basecampserver.tech/sensors?node_id={id}&from=1667465705"


@app.route("/")
def dashboard():
    data = getData()

    labels = [
        datetime.fromtimestamp(row["timestamp"]).strftime("%Y-%m-%d %H:%M")
        for row in data
    ]
    temperatures = [round(row["temperature"], 2) for row in data]
    humidity = [round(row["humidity"], 1) for row in data]
    pressure = [round(row["pressure"], 2) for row in data]

    statistics = {
        "temperature": {
            "average": display_average(temperatures),
            "min": min(temperatures),
            "max": max(temperatures),
            "std_dev": display_standard_deviation(temperatures),
        },
        "humidity": {
            "average": display_average(humidity),
            "min": min(humidity),
            "max": max(humidity),
            "std_dev": display_standard_deviation(humidity),
        },
        "pressure": {
            "average": display_average(pressure),
            "min": min(pressure),
            "max": max(pressure),
            "std_dev": display_standard_deviation(pressure),
        },
    }

    return render_template(
        "dashboard.html",
        labels=labels,
        temperatures=temperatures,
        humidity=humidity,
        pressure=pressure,
        statistics=statistics,
    )


@app.route("/data")
def fetchData():
    data = getData()

    labels = [
        datetime.fromtimestamp(row["timestamp"]).strftime("%Y-%m-%d %H:%M")
        for row in data
    ]
    temperatures = [round(row["temperature"], 2) for row in data]
    humidity = [round(row["humidity"], 1) for row in data]
    pressure = [round(row["pressure"], 2) for row in data]

    statistics = {
        "temperature": {
            "average": display_average(temperatures),
            "min": min(temperatures),
            "max": max(temperatures),
            "std_dev": display_standard_deviation(temperatures),
        },
        "humidity": {
            "average": display_average(humidity),
            "min": min(humidity),
            "max": max(humidity),
            "std_dev": display_standard_deviation(humidity),
        },
        "pressure": {
            "average": display_average(pressure),
            "min": min(pressure),
            "max": max(pressure),
            "std_dev": display_standard_deviation(pressure),
        },
    }

    return {
        "statistics": statistics,
        "temperatures": temperatures,
        "humidity": humidity,
        "pressure": pressure,
        "labels": labels,
    }


def getData():
    r = requests.get(url=getUrl)
    data = r.json()

    return data


def display_average(data):
    total = 0
    index = 0
    for i in data:
        total += i
        index += 1
    avg = total / index
    return round(avg, 2)


def display_standard_deviation(data):
    return round(stdev(data, display_average(data)), 2)
