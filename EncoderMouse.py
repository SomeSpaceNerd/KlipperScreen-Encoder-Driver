from gpiozero import RotaryEncoder, Button
from evdev import UInput, ecodes as e
import time
import signal

# Define GPIO pins
pin_a = 27
pin_b = 17
pin_button = 22

# Mode: 0 for X-axis, 1 for Y-axis
mode = 0

# Initialize UInput device
capabilities = {
    e.EV_KEY: [e.BTN_LEFT, e.BTN_RIGHT],
    e.EV_REL: [e.REL_X, e.REL_Y],
}
ui = UInput(capabilities)

def button_hold():
    ui.write(e.EV_KEY, e.BTN_LEFT, 1)
    ui.syn()
    time.sleep(0.25)
    ui.write(e.EV_KEY, e.BTN_LEFT, 0)
    ui.syn()

def button_pressed():
    global mode
    mode = 1 - mode  # Toggle between 0 and 1

def move_mouse():
    global encoder
    steps = encoder.steps
    movement_amount = 8  # Adjust the movement multiplier here
    if mode == 0:
        if steps > 0:
            ui.write(e.EV_REL, e.REL_X, -movement_amount)
        elif steps < 0:
            ui.write(e.EV_REL, e.REL_X, movement_amount)
    elif mode == 1:
        if steps > 0:
            ui.write(e.EV_REL, e.REL_Y, movement_amount)
        elif steps < 0:
            ui.write(e.EV_REL, e.REL_Y, -movement_amount)
    ui.syn()
    encoder.steps = 0  # Reset encoder steps after each move

# Set up GPIO devices
encoder = RotaryEncoder(pin_a, pin_b)
encoder.when_rotated = move_mouse

button = Button(pin_button)
button.held_time = 0.75
button.when_held = button_hold
button.when_pressed = button_pressed

# Keep the script running
signal.pause()
