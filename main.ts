input.onButtonPressed(Button.A, function () {
    charm = charms[randint(0, charms.length - 1)]
    basic.showString(charm)
    basic.pause(1000)
    if (charm == "Accio") {
        basic.showString("Exchange Place with")
    } else if (charm == "Stupefy") {
        basic.showString("Loose a turn")
    } else if (charm == "Descendo") {
        basic.showString("Backwards 3 places")
    }
    basic.pause(1000)
})
input.onButtonPressed(Button.B, function () {
    curse = curses[randint(0, curses.length - 1)]
    basic.showString(curse)
    basic.pause(1000)
    if (curse == "Avada Kedavra") {
        basic.showString("Return to Start")
    } else if (curse == "Crucio") {
        basic.showString("Loose 2 turns")
    } else if (curse == "Expulso") {
        basic.showString("Backwards 5 places")
    }
    basic.pause(1000)
})
// if (Math.randomBoolean()) {
// basic.showIcon(IconNames.Diamond)
// basic.pause(1000)
// basic.showString("Double Turn!")
// basic.pause(1000)
// }
input.onGesture(Gesture.Shake, function () {
    dice = randint(1, 6)
    basic.showNumber(dice)
    basic.pause(2000)
    basic.clearScreen()
})
let dice = 0
let curse = ""
let charm = ""
let curses: string[] = []
let charms: string[] = []
charms = ["Accio", "Stupefy", "Descendo"]
curses = ["Avada Kedavra", "Crucio", "Expulso"]
basic.showString("Harry Potter Maze")
basic.clearScreen()
