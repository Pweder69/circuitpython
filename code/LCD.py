import board
import time
import pwmio
from digitalio import DigitalInOut, Direction, Pull
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)
#object declerations 

btn = DigitalInOut(board.D8)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT
switch.pull = Pull.DOWN
#Declaring the pins pull down as to detect signal change 

changeVal =1
printedVal =0
btnState = False
#Global Vars :(

def switchManager():
    if switch.value ==True:
        return  1
    else:
       return  -1
    #manages the switch and the value multiplier.

def buttonManager():
    global printedVal
    global btnState
    global changeVal
    changeVal = switchManager()
    if btn.value != btnState:
        #catches the loop and halts activation untill button is released.
        btnState = False
    if btn.value == True and btnState == False:
        #changes the value(printedVal) based on switchManager()/switch
        printedVal += changeVal
        btnState = True
    #controlls the button press as to only allow one activation after press

def lcdUpdate(change,print):
    lcd.print(f" Value:{print}\n switch:{change}")
    time.sleep(.1)
    lcd.clear()
    #Just prints the values to the lcd using f String.

while True:
    buttonManager()
    lcdUpdate(changeVal,printedVal)

    print(f"printed Value:{printedVal}")
    print(f"changeVal:{switchManager()}")


#By Paul Weder
    
    


