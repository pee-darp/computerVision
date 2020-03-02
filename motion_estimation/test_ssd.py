#! /usr/bin/python3
import numpy as np
import os
import sys
sys.path.insert(1, "/home/spradeep/pradeep/computerVision/lib")
from ssd import *

a = 2 * np.ones([5,5])
b = np.ones([3,3])
print(sumsqdiff3(a,b))
