# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Blink example for boards with ONLY a NeoPixel LED (e.g. without a built-in red LED).
Includes QT Py and various Trinkeys.

Requires two libraries from the Adafruit CircuitPython Library Bundle.
Download the bundle from circuitpython.org/libraries and copy the
following files to your CIRCUITPY/lib folder:
* neopixel.mpy
* adafruit_pixelbuf.mpy

Once the libraries are copied, save this file as code.py to your CIRCUITPY
drive to run it.
"""
import time
import board
import neopixel

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
print("Hello, world!")
"""
while True:
    pixels.fill((255, 255, 0))
    time.sleep(0.5)
    pixels.fill((0, 255, 255))
    time.sleep(0.5)
    pixels.fill((255, 0, 255))
    time.sleep(0.5)
"""
#pixels.fill((255,0,0))
#while True: pass

import keypad
import board

keyboard = Keyboard(usb_hid.devices)

key_number_to_keycode = [
    None,
    Keycode.B,    # R1C2
    Keycode.C,    # R1C3
    Keycode.A,    # R1C1
    None,
    None,
    Keycode.D,    # R2C1
    Keycode.E,    # R2C2
    Keycode.F,    # R2C3
    Keycode.G,    # R3C1
    Keycode.H,    # R3C2
    Keycode.I,    # R3C3
]

km = keypad.KeyMatrix(
    row_pins=(board.D9, board.D1, board.D4, board.A3),
    column_pins=(board.A2, board.A1, board.A0),
    columns_to_anodes=True,
)

while True:
    event = km.events.get()
    if not event:
        continue

    keycode = key_number_to_keycode[event.key_number]
    print(keycode, event.pressed)
    try:
        if event.pressed:
            keyboard.press(keycode)
        else:
            keyboard.release(keycode)
    except ValueError:
        # > 6 keys concurrently
        keyboard.release_all()

    time.sleep(0.005)    # ~200 Hz
