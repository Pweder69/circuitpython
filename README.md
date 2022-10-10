# CircuitPython

This repository will actually serve as a aid to help you get started with your own template. You should copy the raw form of this readme into your own, and use this template to write your own. If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).

## Table of Contents

* [Table of Contents](#TableOfContents)

* [Hello_CircuitPython](#Hello_CircuitPython)

* [CircuitPython_Servo](#CircuitPython_Servo)

* [CircuitPython_LCD](#CircuitPython_LCD)

* [NextAssignmentGoesHere](#NextAssignment)

---

  

## Hello_CircuitPython

  

### Description

In this assignment we were tasked with lighting on the led on the metro board using the built in led called the Neopixle.

### Code 

```python

import board  
import neopixel  
  
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5   
  
print("Make it red!")
  
while True:  
    dot.fill((0, 0, 255))

```

  
  

### Evidence
![unnamed](https://user-images.githubusercontent.com/113122312/193068923-696fccd2-2f26-430c-8853-429a9b058300.jpg)
Credit: https://github.com/Jpark27614 
  



  
  
  

### Wiring
The Neopixle didnt require wiring becasue it was a built in LEDto the board 

  

### Reflection
The hardest part of this challenge was getting the libraries to work as the boards had an outdated lib folder and didnt contain the same 
  
  
  
  

## CircuitPython_Servo

  

### Description & Code

  

```python

Code goes here

```

  

### Evidence

  

Pictures / Gifs of your work should go here. You need to communicate what your thing does.

  

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

  

def  switchManager():

if switch.value ==True:

return  1

else:

return -1

#manages the switch and the value multiplier.

  

def  buttonManager():

global printedVal

global btnState

global changeVal

changeVal = switchManager()

if btn.value != btnState:

#catches the loop and halts activation untill button is released.

btnState = False

if btn.value == True  and btnState == False:

#changes the value(printedVal) based on switchManager()/switch

printedVal += changeVal

btnState = True

#controlls the button press as to only allow one activation after press

  

def  lcdUpdate(change,print):

lcd.print(f" Value:{print}\n switch:{change}")

time.sleep(.1)

lcd.clear()

#Just prints the values to the lcd using f String.

  

while  True:

buttonManager()

lcdUpdate(changeVal,printedVal)

  

print(f"printed Value:{printedVal}")

print(f"changeVal:{switchManager()}")

  
  

#By Paul Weder

  
  

```

  

### Evidence

  
  
  

Pictures / Gifs of your work should go here. You need to communicate what your thing does.

  

### Wiring

![LCD_bb](https://user-images.githubusercontent.com/112962227/193609909-9bf87edb-7455-47b3-aca5-481af60a4af1.png)

  

### Reflection

This assigment was a good intro to reintoduce buttons into our common workflow. It also allowed us to see the contrast between python and the arduino C++ addapation.

  
  

## NextAssignment

  

### Description & Code

  

```python

Code goes here

  

```

  

### Evidence

  

### Wiring

  

### Reflection