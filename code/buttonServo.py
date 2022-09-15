import time
import board
import time
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

btn1 = DigitalInOut(board.D8)
btn1.direction = Direction.INPUT
btn1.pull = Pull.UP

btn2 = DigitalInOut(board.D9)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP

my_servo = servo.Servo(pwm)
angle = 0

while True:
    if not  btn2.value:
        my_servo.angle += 5
        
    if not btn1.value:
        my_servo.angle -= 5     
        

    time.sleep(0.1) # sleep for debounce