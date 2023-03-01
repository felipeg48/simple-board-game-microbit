def on_button_pressed_a():
    global charm
    charm = charms[randint(0, len(charms) - 1)]
    basic.show_string(charm)
    basic.pause(1000)
    if charm == "Accio":
        basic.show_string("Exchange Place with")
    elif charm == "Stupefy":
        basic.show_string("Loose a turn")
    elif charm == "Descendo":
        basic.show_string("Backwards 3 places")
    basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global curse
    curse = curses[randint(0, len(curses) - 1)]
    basic.show_string(curse)
    basic.pause(1000)
    if curse == "Avada Kedavra":
        basic.show_string("Return to Start")
    elif curse == "Crucio":
        basic.show_string("Loose 2 turns")
    elif curse == "Expulso":
        basic.show_string("Backwards 5 places")
    basic.pause(1000)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global double
    double = randint(1, 6)
    basic.show_number(double)
    basic.pause(1000)
    if Math.random_boolean():
        basic.show_icon(IconNames.DIAMOND)
        basic.pause(1000)
        basic.show_string("Double Turn!")
        basic.pause(1000)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

double = 0
curse = ""
charm = ""
curses: List[str] = []
charms: List[str] = []
basic.show_string("Harry Potter Maze")
charms = ["Accio", "Stupefy", "Descendo"]
curses = ["Avada Kedavra", "Crucio", "Expulso"]