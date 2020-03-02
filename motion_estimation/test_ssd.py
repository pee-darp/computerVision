#! /usr/bin/python3
import numpy as np
import os
import sys
sys.path.insert(1, "/home/spradeep/pradeep/computerVision/lib")
from ssd import *

a = 2 * np.random.rand(1080,1920)
b = np.random.rand(10,10)
print(sumsqdiff3(a,b))
