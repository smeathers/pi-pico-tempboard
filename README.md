# pi-pico-tempboard
Goofing around with the new Raspberry Pi Pico

Example code takes the value from the Pico's temperature sensor and types it out 10 times via USB HID onto the host computer.

1. Download .uf2 file from https://circuitpython.org/board/raspberry_pi_pico/
2. Plug Pico into USB port of computer while holding down the button.
3. Copy .uf2 to the newly mounted USB storage device (after copy is complete device will reboot)
4. Download Adafruit's CircuitPython HID from https://github.com/adafruit/Adafruit_CircuitPython_HID
5. Copy the "adafruit_hid" folder from step 4 to the "lib" folder on the new CIRCUITPY USB storage device.
6. !!! BEFORE the next step have a text editor window open ready to switch to as once code.py file has been updated it will start running on the Pico.
7. Replace code.py in CIRCUITPY USB storage device with version from this project.
