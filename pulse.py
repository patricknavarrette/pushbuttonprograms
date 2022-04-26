from gpiozero import LED, Button
from signal import pause
from gpiozero import PWMLED

led = PWMLED(24)
button = Button(23)

while True:
    if button.is_pressed:
        led.off
    else:
        led.pulse()



pause()
