"""
--------------------------------------------------------------------------
Rep Counter
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

Rep Counter

  This driver analyzes x,y,z accelerometer data to determine when a user has
  performed a repetition (rep) of an exercise.
  
Software API

    __init__(threshold_multiplier)
        - Sets threshold multiplier as given input value (default = 0.6)
        - This is currently not being utilized but can be to have rep
        detection cutoff to be based on gathered data instead of a hard-coded
        value
        
    process_data(accel_data)
      - Takes x,y,z acclerometer data and processes it to find peaks of
      acceleration magnitude
      - Acceleration magnitude peaks above defined threshold are counted as
      reps
    

"""
import numpy as np
from scipy.signal import find_peaks

class RepCounter:
    def __init__(self, threshold_multiplier=0.6):
        self.threshold_multiplier = threshold_multiplier

    def process_data(self, accel_data):
        accel_magnitude = np.sqrt([x**2 + y**2 + z**2 for x, y, z in accel_data])
        adjusted_accel_magnitude = np.maximum(accel_magnitude - 8500, 0)
        #print("mag",adjusted_accel_magnitude[-1])
        peaks, _ = find_peaks(adjusted_accel_magnitude, distance=50)
        adjusted_peaks = adjusted_accel_magnitude[peaks]
        #threshold_height = self.threshold_multiplier * np.mean(adjusted_peaks)
        threshold_height = 2500  # Fixed threshold value
        #print("thresh",threshold_height)
        reps = np.sum(adjusted_peaks > threshold_height)

        return adjusted_accel_magnitude, peaks, adjusted_peaks, threshold_height, reps
