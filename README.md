# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here

Here's how you make code look like code:

```python
Code goes here

```


### Evidence


![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone, if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

```python
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
    
    





```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
