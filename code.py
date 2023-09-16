import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

kbd = Keyboard(usb_hid.devices)
sensor = DigitalInOut(board.D7)
sensor.direction = Direction.INPUT
sensor.pull = Pull.UP

while True:
    print(sensor.value)
    if sensor.value == False:
        kbd.send(Keycode.ENTER)
        time.sleep(0.1)
        print("Enter pressed, photo taken")
        kbd.release_all()
    else:
        pass
    time.sleep(1)
