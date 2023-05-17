import board
from analogio import AnalogIn, AnalogOut 
import simpleio
import pwmio

control = pwmio.PWMOut(board.D8, duty_cycle = 2 ** 15)


pot = AnalogIn(board.A0)

while True:
    print(int(pot.value))
    control.duty_cycle = simpleio.map_range(pot.value,0,65355,0,255)