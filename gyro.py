#!/usr/bin/env python

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# BP.set_sensor_type configures the BrickPi3 for a specific sensor.
# BP.PORT_1 specifies that the sensor will be on sensor port 1.
# There are three modes for the Gyro sensor
# BP.Sensor_TYPE.EV3_GYRO_ABS mode. The sensor will show only the degrees from its initial zeroed position.
# BP.Sensor_TYPE.EV3_GYRO_DPS mode. The sensor will show only the degrees per second rotation.
# BP.Sensor_TYPE.EV3_GYRO_ABS_DPS mode. The sensor will show the degrees from its initial zeroed position and the degrees per second of rotation.
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_GYRO_ABS_DPS)
# Pause to wait for sensor setup to finish

time.sleep(2)

def auto_correct(Indeg):
    deg = BP.get_sensor(BP.PORT_1)[0]
    x = deg > Indeg
    y = deg < Indeg 
    if x:
        print("left")
        print(x)

    elif y:
        print("right")
        print(y)
    else:
        print("No Correction")
        pass
try:
    while True:
        
        Indeg = BP.get_sensor(BP.PORT_1)[0]
    
        try:
            for():
                x = 
                try:
                    auto_correct(Indeg)
            
                except brickpi3.SensorError as error:
                    print(error)
        
                time.sleep(0.05)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.
                
        except KeyboardInterrupt:
            BP.reset_all() 

except KeyboardInterrupt:
    BP.reset_all() 
