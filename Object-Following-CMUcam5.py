import RPi.GPIO as GPIO  
from pixy import *
from ctypes import *
import sys
import tty
import termios
import time

# Pixy Python SWIG get blocks example #

print ("Pixy Python SWIG Example -- Get Blocks")
mode = GPIO.getmode()
in1 = 23
in2 = 24
enA = 25
in3 = 17
in4 = 27
enB = 22
temp1=1
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p1=GPIO.PWM(enA,2000)
p2=GPIO.PWM(enB,2000)
p1.start(50)
p2.start(50)
# Initialize Pixy Interpreter thread #
print ("w : Accelerate")
print ("s : Brake")
print ("a/d :Steering")
pixy_init()

class Blocks (Structure):
  _fields_ = [ ("type", c_uint),
               ("signature", c_uint),
               ("x", c_uint),
               ("y", c_uint),
               ("width", c_uint),
               ("height", c_uint),
               ("angle", c_uint) ]

blocks = BlockArray(100)
frame  = 0


# Wait for blocks #
while 1:

  count = pixy_get_blocks(100, blocks)

  if count > 0:
    # Blocks found #
    frame = frame + 1
    for index in range (0, count):
        if(blocks[index].x>=112 and blocks[index].x<=198):
            print("forward")
            p1.ChangeDutyCycle(55)
            p2.ChangeDutyCycle(57)
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            time.sleep(1)
            temp1=1
        elif(blocks[index].x<112):
            print('left')
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            time.sleep(1)
            temp1=1
        elif(blocks[index].x>198):
            print('Right')
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            temp1=1
            time.sleep(1)
        elif(blocks[index].signature != 1):
            print('Back to Manual Mode')
            break
        else:
            print('Line not Found')
            break
            
                      
          
    