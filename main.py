def L():
    basic.show_arrow(ArrowNames.WEST)
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, -255, SuperBit.enMotors.M2, 255)
    SuperBit.motor_run_dual(SuperBit.enMotors.M3, 255, SuperBit.enMotors.M4, -255)
    basic.pause(100)
    BB()
def spinleft():
    basic.show_arrow(ArrowNames.NORTH_WEST)
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, -255, SuperBit.enMotors.M2, -255)
    SuperBit.motor_run_dual(SuperBit.enMotors.M3, 255, SuperBit.enMotors.M4, 255)
    BB()

def on_received_number(receivedNumber):
    if receivedNumber == 1:
        F()
        basic.show_arrow(ArrowNames.NORTH)
    elif receivedNumber == 2:
        L()
        basic.show_arrow(ArrowNames.EAST)
    elif receivedNumber == 3:
        B()
        basic.show_arrow(ArrowNames.SOUTH)
    elif receivedNumber == 4:
        R()
        basic.show_arrow(ArrowNames.WEST)
    elif receivedNumber == 5:
        SuperBit.motor_stop_all()
    elif receivedNumber == 6:
        spinright()
        basic.show_arrow(ArrowNames.NORTH_EAST)
    elif receivedNumber == 7:
        spinleft()
        basic.show_arrow(ArrowNames.NORTH_WEST)
    elif receivedNumber == 8:
        SuperBit.motor_stop_all()
        SuperBit.music(SuperBit.enMusic.PRELUDE)
        basic.show_icon(IconNames.SMALL_HEART)
    elif receivedNumber == 9:
        basic.show_icon(IconNames.HOUSE)
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    else:
        basic.show_icon(IconNames.DUCK)
radio.on_received_number(on_received_number)

def F():
    basic.show_arrow(ArrowNames.NORTH)
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, 255, SuperBit.enMotors.M2, 255)
    SuperBit.motor_run_dual(SuperBit.enMotors.M3, 255, SuperBit.enMotors.M4, 255)
    basic.pause(100)
    BB()
def B():
    basic.show_arrow(ArrowNames.SOUTH)
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, -255, SuperBit.enMotors.M2, -255)
    SuperBit.motor_run_dual(SuperBit.enMotors.M3, -255, SuperBit.enMotors.M4, -255)
    basic.pause(100)
    BB()
def BB():
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    basic.pause(200)
    strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    basic.pause(200)
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.pause(200)
    strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    basic.pause(200)
    strip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
    basic.pause(200)
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
    basic.pause(200)
def R():
    basic.show_arrow(ArrowNames.EAST)
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, 255, SuperBit.enMotors.M2, -255)
    SuperBit.motor_run_dual(SuperBit.enMotors.M3, -255, SuperBit.enMotors.M4, 255)
    basic.pause(100)
    BB()
def spinright():
    basic.show_arrow(ArrowNames.NORTH_EAST)
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, 255, SuperBit.enMotors.M2, 255)
    SuperBit.motor_run_dual(SuperBit.enMotors.M3, -255, SuperBit.enMotors.M4, -255)
    BB()
strip: neopixel.Strip = None
radio.set_group(13)
basic.show_icon(IconNames.YES)
SuperBit.motor_stop_all()
basic.show_arrow(ArrowNames.NORTH)
strip = neopixel.create(DigitalPin.P12, 4, NeoPixelMode.RGB)
range2 = strip.range(0, 3)

def on_forever():
    basic.show_icon(IconNames.ANGRY)
    SuperBit.servo(SuperBit.enServo.S7, 0)
    basic.pause(2000)
    SuperBit.servo(SuperBit.enServo.S7, 180)
    basic.pause(2000)
basic.forever(on_forever)
