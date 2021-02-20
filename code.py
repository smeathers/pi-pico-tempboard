import time
import usb_hid
import microcontroller
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

time.sleep(0.5) # allows time for device driver to load in OS before typing starts.

#while True:
for _ in range(10):
    #keyboard_layout.write("Hello World\n")
    keyboard_layout.write(str(round(microcontroller.cpu.temperature, 1)) + ",\n")
    time.sleep(1)

# https://github.com/adafruit/Adafruit_CircuitPython_HID
# 
