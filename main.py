def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P0, 1)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 0)
    basic.show_string("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)
    basic.show_string("8")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    basic.show_string("B")
input.on_button_pressed(Button.B, on_button_pressed_b)
