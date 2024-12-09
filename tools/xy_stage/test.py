# %%
import os
import time
from random import randrange, uniform

from Rx_loading import run
xy_addr = 'ASRL/dev/ttyUSB0::INSTR'
# create random Rx position
""""
Rx = ['Rx'+str(randrange(5)) for i in range(200)]
with open('Rx_loading_sequence2.dat','w') as f:
    for i in range(len(Rx)):
        f.write(Rx[i]+'\n')
"""
Rx = []
with open('Rx_loading_sequence2.dat','r') as f:
    for line in f:
        Rx.append(line.split('\r')[0])
#print(Rx)
# %%

time.sleep(20)
for item in Rx:
    Rx_position = run(xy_addr, RxNo = item)
    time.sleep(3)
    with open('Rx_movement2.log','a') as f:
        f.write(Rx_position+'\n')

# %%
