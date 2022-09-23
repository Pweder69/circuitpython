import board
import time
import pwmio
from digitalio import DigitalInOut, Direction, Pull

btn = DigitalInOut(board.D8)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT
switch.pull = Pull.DOWN

changeVal =1
printedVal =0
btnState = False
LBtnstate = False

switchState = False
LSwitchstate =False


while True:
    LSwitchstate 
    if switch.value == True and switchState ==False:
        changeVal *-1
        print("changed")
        
        
    


    if btn.value == True and btnState == False:
        printedVal += changeVal
        btnState = True


    print(printedVal)
    print(changeVal)
    time.sleep(.1)
    
        

