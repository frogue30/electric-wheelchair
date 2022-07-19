import RPi.GPIO as GPIO  
from ctypes import *
import sys
import tty
import termios
import time


mode = GPIO.getmode()
in1 = 23
in2 = 24
enA = 25
in3 = 27
in4 = 17
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


def getch():
    fd = sys.stdin.fileno()
    old_settings=termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch=sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
    return ch
# Wait for blocks #
while 1:
    char = getch()        
    if char=="w":
        print ("Forward")
        p1.ChangeDutyCycle(65)
        p2.ChangeDutyCycle(65)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
    elif char=="d":
        print("Turn Left")                          
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
              
    elif char=="a":
        print("Turn Right")          
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
              
    elif char=="s":
        print ("Stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        
    elif char =="x":
        print("Program Ended")
        break
              
          
    char==""
    