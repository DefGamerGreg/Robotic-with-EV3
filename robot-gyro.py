#!/usr/bin/env python

from __future__ import print_function 
from __future__ import division

import time     # import time library
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create BrickPi3 class

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_GYRO_ABS_DPS)
time.sleep(2)

def getchar():
   #Returns a single character from standard input
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

def speed_control(z):
      if z > 100:
         z = 100

      if z < -100:
         z = -100

      return z         


def speed(v1,v2,t):
   valuex = v1
   valuey = v2
   
   BP.set_motor_power(BP.PORT_A, v1)
   BP.set_motor_power(BP.PORT_D, v2)
   # Wait t seconds
   time.sleep(t)
   x = 0
   y = 0
   BP.set_motor_power(BP.PORT_A, 0)
   BP.set_motor_power(BP.PORT_D, 0)

   return v1, v2, t
   time.sleep(0.05)

def stop_motor():
   BP.set_motor_power(BP.PORT_A, 0)
   BP.set_motor_power(BP.PORT_D, 0)


def auto_correct(v1,v2,t):
   x = 0
   deg = BP.get_sensor(BP.PORT_1)[0]
   if deg > x:
      print(deg)
      x = x + 10

   elif deg < x:
      print(deg)
      y = y + 10
      
   else:
      print("0")
      pass
   
   time.sleep(t)
   x = 0
   y = 0
   BP.set_motor_power(BP.PORT_A, 0)
   BP.set_motor_power(BP.PORT_D, 0)

   return v1, v2, t
   time.sleep(0.05)
    
      

   
try:
   x = 0
   y = 0
   key = 'w'

   while key != '-': 
      key = getchar()
      print("Stear" + key)
      print(BP.get_sensor(BP.PORT_1)[0])

      if key == 'w':
         x = x + 10
         y = y + 10
         
      elif key == 's':
         x = x - 10
         y = y - 10
      elif key == 'a':
          x = x - 21
          y = y + 25
      elif key == 'd':
          x = x + 25
          y = y - 21
      elif key == " ":
          x = 0
          y = 0
      elif key == '8':
          g = 0
          BP.set_motor_power(BP.PORT_A, 20)
          BP.set_motor_power(BP.PORT_D, 20)
          deg = BP.get_sensor(BP.PORT_1)[0]
          if deg > g:
             x = 30
             y - 10

          elif deg < g:
             y + 10
             x - 10
      
          else:
             print("0")
             pass
            
      elif key == '2':
          speed(-60,-60,2)
      elif key == '5':
          stop_motor()
      elif key == '4':
          speed(-10,73,2.33)
      elif key == '6':
          speed(73,-10,2.33)


      x = speed_control(x)
      y = speed_control(y)
          
      BP.set_motor_power(BP.PORT_A, x)
      BP.set_motor_power(BP.PORT_D, y)



         
   BP.set_motor_power(BP.PORT_A, 0)
   BP.set_motor_power(BP.PORT_D, 0)


   
      

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
   BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.
