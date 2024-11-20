function L () {
    basic.showArrow(ArrowNames.West)
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M1,
    -255,
    SuperBit.enMotors.M2,
    255
    )
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M3,
    255,
    SuperBit.enMotors.M4,
    -255
    )
    basic.pause(100)
    BB()
}
function spinleft () {
    basic.showArrow(ArrowNames.NorthWest)
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M1,
    -255,
    SuperBit.enMotors.M2,
    -255
    )
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M3,
    255,
    SuperBit.enMotors.M4,
    255
    )
    BB()
}
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        F()
        basic.showArrow(ArrowNames.North)
    } else if (receivedNumber == 2) {
        L()
        basic.showArrow(ArrowNames.East)
    } else if (receivedNumber == 3) {
        B()
        basic.showArrow(ArrowNames.South)
    } else if (receivedNumber == 4) {
        R()
        basic.showArrow(ArrowNames.West)
    } else if (receivedNumber == 5) {
        SuperBit.MotorStopAll()
    } else if (receivedNumber == 6) {
        spinright()
        basic.showArrow(ArrowNames.NorthEast)
    } else if (receivedNumber == 7) {
        spinleft()
        basic.showArrow(ArrowNames.NorthWest)
    } else if (receivedNumber == 8) {
        SuperBit.MotorStopAll()
        SuperBit.Music(SuperBit.enMusic.prelude)
        basic.showIcon(IconNames.SmallHeart)
    } else if (receivedNumber == 9) {
        basic.showIcon(IconNames.House)
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
    } else {
        basic.showIcon(IconNames.Duck)
    }
})
function F () {
    basic.showArrow(ArrowNames.North)
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M1,
    255,
    SuperBit.enMotors.M2,
    255
    )
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M3,
    255,
    SuperBit.enMotors.M4,
    255
    )
    basic.pause(100)
    BB()
}
function B () {
    basic.showArrow(ArrowNames.South)
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M1,
    -255,
    SuperBit.enMotors.M2,
    -255
    )
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M3,
    -255,
    SuperBit.enMotors.M4,
    -255
    )
    basic.pause(100)
    BB()
}
function BB () {
    strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
    basic.pause(200)
    strip.showColor(neopixel.colors(NeoPixelColors.Orange))
    basic.pause(200)
    strip.showColor(neopixel.colors(NeoPixelColors.Green))
    basic.pause(200)
    strip.showColor(neopixel.colors(NeoPixelColors.Indigo))
    basic.pause(200)
    strip.showColor(neopixel.colors(NeoPixelColors.Purple))
    basic.pause(200)
    strip.showColor(neopixel.colors(NeoPixelColors.Red))
    basic.pause(200)
}
function R () {
    basic.showArrow(ArrowNames.East)
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M1,
    255,
    SuperBit.enMotors.M2,
    -255
    )
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M3,
    -255,
    SuperBit.enMotors.M4,
    255
    )
    basic.pause(100)
    BB()
}
function spinright () {
    basic.showArrow(ArrowNames.NorthEast)
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M1,
    255,
    SuperBit.enMotors.M2,
    255
    )
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M3,
    -255,
    SuperBit.enMotors.M4,
    -255
    )
    BB()
}
let strip: neopixel.Strip = null
radio.setGroup(121)
basic.showIcon(IconNames.Yes)
basic.showArrow(ArrowNames.North)
strip = neopixel.create(DigitalPin.P12, 4, NeoPixelMode.RGB)
let range = strip.range(0, 3)
basic.forever(function () {
    basic.showIcon(IconNames.Angry)
})
