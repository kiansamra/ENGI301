"""
--------------------------------------------------------------------------
Main
--------------------------------------------------------------------------
License:   
Copyright 2021-2023 - Kian Samra

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Main

  This centralized script runs all relevant drivers of the exercise tracker to
  allow the user to turn on and operate the exercise tracker.  It allows the
  user to turn tracking on/off with a switch, perform exercises and count reps, 
  receive feedback if a rep is completed with a green LED and a live count of
  reps on a 16x2 LCD display.

"""

import time
import csv
import numpy as np
from accelerometer_manager import AccelerometerManager
from rep_counter import RepCounter
from button import Button
from led import LED
from LCD import LCD

# Initialize LED GPIO controller
switch = Button("P2_2") 

rep_counter = RepCounter(threshold_multiplier=0.65)
# Initialize the accelerometer manager
accel_manager = AccelerometerManager(bus_number=1, device_address=0x68)
accel_manager.initialize()

# Initialize LED
led = LED("P2_4")

# Initialize LCD
lcd = LCD("P2_18", "P2_10", "P2_6", "P2_8", "P1_4", "P1_2", 16, 2)

# Create and open a CSV file for writing
with open('accelerometer_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['X', 'Y', 'Z'])  # Write headers to the CSV file

    accel_data = []
    prev_reps = 0  # Keep track of the previous rep count
    
    # Continuously read accelerometer data
    while True:
        if switch.is_pressed():
            x, y, z = accel_manager.readData()
            #print(f"Accelerometer Data - X: {x}, Y: {y}, Z: {z}")
            writer.writerow([x, y, z])
            
            new_data = [x, y, z]  # Store as a list, not a numpy array
            accel_data.append(new_data)
            #print("acc data",accel_data)
    
            adjusted_accel_magnitude, peaks, adjusted_peaks, threshold_height, reps = rep_counter.process_data(accel_data)
            
            print(f'Total Repetitions: {reps}')
    
            if reps > prev_reps:  # Check if the rep count increased by 1
                prev_reps = reps  # Update the previous rep count
                # Turn LED on
                led.on()
                lcd.clear()  # Clear the LCD
                lcd.message(f'Rep Count: {reps}')  # Display rep count on LCD
                time.sleep(0.5)  # Wait for 0.5 seconds
                # Turn LED off
                led.off()
            
                
            time.sleep(0.01) # 100Hz
            
        else:
            # If switch is not pressed, reset rep count and clear accel_data
            rep_counter = RepCounter(threshold_multiplier=0.65)
            accel_data = []
            led.off()
            prev_reps = 0
            lcd.clear()