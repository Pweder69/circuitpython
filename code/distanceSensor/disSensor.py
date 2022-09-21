import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)




def getRgb():
    color = [0,0,0]
    if dis < 5:
        color[0] = 255                                  #R
        color[1] = 0                                    #G
        color[2] = 0                                    #B
    elif dis <=20:
        color[0] = simpleio.map_range(dis,5,20,255,0)   #R
        color[1] = 0                                    #G
        color[2] = simpleio.map_range(dis,5,20,0,255)   #B
    elif dis <=35:
        color[0] = 0                                    #R 
        color[1] = simpleio.map_range(dis,20,35,0,255)   #G
        color[2] = simpleio.map_range(dis,20,35,255,0)   #B
    return color
## manages the color and apropriatly assigns the color values based on the distance. 


while True:
    try:
        dis = sonar.distance
        print((sonar.distance,))
        dot.fill(getRgb())
    except RuntimeError:
        print("Retrying!")
    time.sleep(.01)
    



'''
Use the HC-SR04 to measure the distance to an object and print that out to your serial monitor or LCD in cm.
Next, you will get the neopixel to turn red when your object is less than 5cm, blue when between 5 and 20cm, and green when farther than 20cm.
For your final version of this code, you'll smoothly shift the color of the onboard neopixel, corresponding to the distance, according to the graphic below.
(Neopixel should stay red when below 5cm and green when above 35cm)
'''