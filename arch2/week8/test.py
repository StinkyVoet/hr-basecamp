from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.scroll_speed = 0.0001

def display_temp():
    while True:
        temp = round(sense.get_temperature())

        sense.show_message(str(temp), scroll_speed=0.075)
#        sleep(1)

try:
    display_temp()
except KeyboardInterrupt:
    sense.show_message("Bye!", scroll_speed=0.05)
    sense.clear()
    quit()
