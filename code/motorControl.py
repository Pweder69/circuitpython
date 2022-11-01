import board
import time
import pwmio
from digitalio import DigitalInOut, Direction, Pull
import simpleio
from analogio import AnalogIn, AnalogOut 

control = AnalogOut(board.A1)


pot = AnalogIn(board.A0)


while True:
    print(int(pot.value))
    control.value = (pot.value)