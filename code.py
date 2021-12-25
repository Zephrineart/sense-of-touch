
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.touch_A2:
        cpx.play_file("purr.wav")
    elif cpx.touch_A4:
        cpx.play_file("meow.wav")
    else:
        cpx.stop_tone()
