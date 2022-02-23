let t = 0
function convertTemperature (t: number) {
    basic.showString("Temperatura u F: ")
    t = t * 1.8 + 32
    basic.showNumber(t)
}
function showTemperature () {
    basic.showString("Temperatura u C: ")
    basic.showNumber(t)
}
input.onButtonPressed(Button.A, function () {
    showTemperature()
})
input.onButtonPressed(Button.B, function () {
    convertTemperature(t)
})
basic.forever(function () {
    t = input.temperature()
})
