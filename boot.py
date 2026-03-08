# boot.py
# Based on https://docs.circuitpython.org/en/latest/shared-bindings/storage/ and
# https://forums.raspberrypi.com/viewtopic.php?p=1885675&sid=64e0dae1bdc714b6e34fae63b5a67293#p1885675
# By cxw42 2026
# SPDX-License-Identifier: MIT

import time

import board
import digitalio
import neopixel
import storage
import usb_cdc

print("boot.py running")

# Check whether R1C1 is held down (programming mode)
is_r1c1_pressed = False

col_pin_id = board.A2
row_pin_id = board.D1

with digitalio.DigitalInOut(col_pin_id) as col_pin:
    col_pin.switch_to_input(pull=digitalio.Pull.UP)  # pull up the column (anode)
    with digitalio.DigitalInOut(row_pin_id) as row_pin:
        row_pin.switch_to_output(False)  # drive the row (cathode) low
        is_r1c1_pressed = not col_pin.value

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

if is_r1c1_pressed:
    # Programming mode
    led.fill((0, 0, 1))

else:
    # Normal mode --- keypad only
    storage.disable_usb_drive()
    led.fill((1, 1, 0))
    usb_cdc.disable()
