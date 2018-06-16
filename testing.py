 
import _string
import sys
import logging
import numpy as np
from numpy.lib.test.test_datasource import valid_baseurl
dt=open("C:/Users/GLSM/Desktop/dataaaa/testing.txt", "r")
dt.columns=['time','user','computer']
dt1=dt.groupby(["user","computer","time"]).count()
print(dt1)
