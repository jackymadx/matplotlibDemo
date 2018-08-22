#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  demo3.py
#  
#  Copyright 2018 jacky <jacky@jacky-U32U>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import platform;
import matplotlib.pyplot as plt

def main(args):
    return 0
    
def perform():
	print("hello") 
print(platform.platform())
print("Python", sys.version)   

if __name__ == '__main__':
      
    perform()
        
    raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
        
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])
print(df)

plt.scatter(df.preTestScore, df.postTestScore, s=300, c=df.female)
plt.show()
    
sys.exit(main(sys.argv))
