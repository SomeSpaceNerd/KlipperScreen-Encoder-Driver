from gpiozero import RotaryEncoder, Button
from evdev import UInput, ecodes as e
import signal

pin_a = 27
pin_b = 17
pin_button = 22

def UpdateMode():
    if mode == 0:
        mode = 1
    elif mode == 1:
        mode = 0
def ButtonPressed():
    ui.write(e.EV_KEY, e.BTN_LEFT, 1)
    ui.syn()
def ButtonReleased():
    ui.write(e.EV_KEY, e.BTN_LEFT, 0)
    ui.syn()
def MoveMouse():
    if mode == 0:
        if encoder.steps > 0:
            ui.write(e.EV_REL, e.REL_X, 1)
        elif encoder.steps < 0:
            ui.write(e.EV_REL, e.REL_X, -1)
    elif mode == 1:
        if encoder.steps > 0:
            ui.write(e.EV_REL, e.REL_Y, 1)
        elif encoder.steps < 0:
            ui.write(e.EV_REL, e.REL_Y, -1)

encoder = RotaryEncoder(pin_a, pin_b)
encoder.when_rotated = MoveMouse
button = Button(pin_button)
button.hold_time = 1
button.when_held = UpdateMode
button.when_pressed = ButtonPressed
button.when_released = ButtonReleased
ui = UInput()
mode = 0

signal.pause()

