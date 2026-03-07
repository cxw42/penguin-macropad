# boot.py
# Based on https://docs.circuitpython.org/en/latest/shared-bindings/storage/ and
# https://forums.raspberrypi.com/viewtopic.php?p=1885675&sid=64e0dae1bdc714b6e34fae63b5a67293#p1885675
# By cxw42 2026
# SPDX-License-Identifier: MIT

import board
import digitalio
import neopixel
import storage
import time

def print_pin(pin, pullup):
    with digitalio.DigitalInOut(pin) as the_pin:
        the_pin.switch_to_input(pull=digitalio.Pull.UP if pullup else digitalio.Pull.DOWN)
        print(pin, "up" if pullup else "down", the_pin.value)

print("boot.py running")

col_pin_id = board.A2
row_pin_id = board.D1

# Check whether R1C1 is held down
is_r1c1_pressed = False
with digitalio.DigitalInOut(col_pin_id) as col_pin:
    col_pin.switch_to_input(pull=digitalio.Pull.UP) # pull up the column (anode)
    with digitalio.DigitalInOut(row_pin_id) as row_pin:
        row_pin.switch_to_output(False) # drive the row (cathode) low
        is_r1c1_pressed = not col_pin.value

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
for i in range(0):
    led.fill((1,0,0))
    time.sleep(0.75)
    led.fill((0,1,0))
    time.sleep(0.75)

#for pin in (board.D9, board.D1, board.D4, board.A3, board.A2, board.A1, board.A0):
#    print_pin(pin, True)
#    print_pin(pin, False)

if is_r1c1_pressed:
    # Programming mode
    led.fill((0,0,1))

else:
    # Normal mode --- keypad only
    #storage.disable_usb_drive()
    led.fill((1,1,0))
