import os
import h5py
import numpy as np

url='D:/work/zzjoProject/bundle/bundle/yield_curve.h5'
print(url)
with h5py.File(url,'r') as f:
    print(f)
    print(f.keys)