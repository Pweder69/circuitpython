import board
import time
import pwmio
from digitalio import DigitalInOut, Direction, Pull
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)


btn = DigitalInOut(board.D8)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT
switch.pull = Pull.DOWN

changeVal =1
printedVal =0
btnState = False


def switchManager():
    if switch.value ==True:
        return  1
    else:
       return  -1

def buttonManager(changeVal):
    global printedVal
    global btnState
    if btn.value != btnState:
        btnState = False
    if btn.value == True and btnState == False:
        printedVal += changeVal
        btnState = True

def lcdUpdate(change,print):
    lcd.print(f" Value:{print}\n switch:{change}")
    time.sleep(.1)
    lcd.clear()

while True:
    buttonManager(switchManager())
    lcdUpdate(changeVal,printedVal)

    print(f"printed Value:{printedVal}")
    print(f"changeVal:{switchManager()}")
    
    


