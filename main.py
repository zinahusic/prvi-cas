t = 0
def convertTemperature(u: number):
    basic.show_string("Temperatura u F: ")
    u = u * 1.8 + 32
    basic.show_number(u)
def showTemperature():
    basic.show_string("Temperatura u C: ")
    basic.show_number(t)

def on_button_pressed_a():
    showTemperature()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    convertTemperature(t)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global t
    t = input.temperature()
basic.forever(on_forever)
