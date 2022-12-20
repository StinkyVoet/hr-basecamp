from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.clear(0, 0, 0)

green = (0, 255, 0)

xpos = 4
ypos = 4

while True:
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":

            # Check which direction
            if event.direction == "up":  # Up arrow
                ypos -= 1
                sense.set_pixel(xpos, ypos, green)
            elif event.direction == "down":  # Down arrow
                ypos += 1
                sense.set_pixel(xpos, ypos, green)
            elif event.direction == "left":  # Left arrow
                xpos -= 1
                sense.set_pixel(xpos, ypos, green)
            elif event.direction == "right":  # Right arrow
                xpos += 1
                sense.set_pixel(xpos, ypos, green)
            elif event.direction == "middle":  # Enter key
                sense.set_pixel(xpos, ypos, green)
    sense.set_pixel(xpos, ypos, green)
