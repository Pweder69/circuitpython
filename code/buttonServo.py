
import board
import time
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

btn1 = DigitalInOut(board.D8)
btn1.direction = Direction.INPUT
btn1.pull = Pull.UP
#definitions for button pins 

btn2 = DigitalInOut(board.D9)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP


my_servo = servo.Servo(pwm)
angle = 0
lock1 = False
lock2 = False


while True:
    if not  btn2.value and lock1 == False:
        lock1 = True
        lock2 = False
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            print(angle)


    if not btn1.value and lock2 == False:
        lock1 = False # locks the turn so that you dont have to 
        lock2 = True
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
            my_servo.angle = angle
            print(angle)

    time.sleep(0.1) # sleep for debounce