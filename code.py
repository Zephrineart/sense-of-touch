
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.touch_A2:
        cpx.play_file("cat.wav")
    else:
        cpx.stop_tone()
