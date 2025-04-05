# 3x3 keypad.  Based on code by Kattni Rembor and Dan Halbert of Adafruit Industries.
# By cxw42 2025
# Matrix scanning: <https://learn.adafruit.com/key-pad-matrix-scanning-in-circuitpython/keymatrix>
# HID: <https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse>
#
# Requires the adafruit_hid library, <https://docs.circuitpython.org/projects/hid/en/latest/index.html>
#
# SPDX-License-Identifier: MIT

import time
import board

import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Keymap.  I had to split row 1 into two row pins because of space constraints.
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

def main():
    print("Hello, world!")

	# Initialize
    km = keypad.KeyMatrix(
        row_pins=(board.D9, board.D1, board.D4, board.A3),
        column_pins=(board.A2, board.A1, board.A0),
        columns_to_anodes=True,
    )

    keyboard = Keyboard(usb_hid.devices)

    while True:
        event = km.events.get()
        if not event:
            continue

        keycode = key_number_to_keycode[event.key_number]
        if not keycode:
            continue

        # Handle the event
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

if __name__ == '__main__':
    main()
