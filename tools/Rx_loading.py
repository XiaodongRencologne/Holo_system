'''
This code only works when the xy-stage has been initialized and 
the Rx mounting points and its pre-loading processes are trained.
'''
# %%
import sys, os, time
import numpy as np
sys.path.append('./instr')
import DNC_IMC
from DNC_IMC import ISEL

import argparse
# %%

# 1. Position of Central Rx mounting point
Rx0=[550.0,550.0]
# 1.2 Offset of pre-loading position from the Rx mounting point.
offset_dy = 100.0 # mm
# 1.3 Loading movement
Loading_dy = 100.0 # mm
Loading_speed = 10.0 # mm/s
Pickup_speed = 10.0  # mm/s
Moving_speed = 30.0  # mm/s
# 2. separated distance of other 4 off-axis Rx points. 
dx = 400.0
dy = 400.0

Rx1 = [Rx0[0]-dx,Rx0[1]+dy]
Rx2 = [Rx0[0]+dx,Rx0[1]+dy]
Rx3 = [Rx0[0]-dx,Rx0[1]-dy]
Rx4 = [Rx0[0]+dx,Rx0[1]-dy]

Rxs = { 'Rx0': Rx0,
       'Rx1': Rx1,
       'Rx2': Rx2,
       'Rx3': Rx3,
       'Rx4': Rx4
    }
# 3. set the forbidden region of each Rx mounting position. 
"""
----xx----               -----xx-----
|        |               |          |
| x(Rx1) |               |   x(Rx2) |
|        |               |          |
----------               ------------

             -----xx----
             |         |
             |  x(Rx0) |
             |         |
             -----------
----xx----               ------xx----
|        |               |          |
| x(Rx3) |               |   x(Rx4) |
|        |               |          |
----------               ------------

'x' is Rx mounting point.
'xx' is Rx pre-loading position.
When the command of 'load' is carried out, the xy-stage moves the arm
downward by 'dy=200mm' to place the Rx to the mounting frame.

The the status of xy-stage is changed to 'loaded'.
""" 
#Forbidden_range=[150,150]

## Methods
# check current position
def check_position(instr):
    current_position = None
    instr.position()
    point = [instr.point[0]*5/1000, instr.point[1]*5/1000 + Loading_dy]
    for key in Rxs.keys():
        if point == Rxs[key]:
            current_position = key
    return current_position

# load Rx
def load(instr):
    instr.moveDown(step=Loading_dy, speed=Loading_speed)
# pick up Rx
def pickUp(instr):
    instr.moveUp(step=Loading_dy, speed=Pickup_speed)
# Move to center pre-loading position
def move_to_Rx0(instr):
    instr.position()
    x = Rx0[0] - instr.point[0]*5/1000
    y = Rx0[1] - instr.point[1]*5/1000
    if y > 0:
        instr.moveUp(step = y, speed = Moving_speed)
        instr.moveRight(step = x, speed = Moving_speed)
    else:
        instr.moveRight(step = x, speed = Moving_speed)
        instr.moveUp(step = y, speed = Moving_speed)
    instr.position()
    position = [instr.point[0]*5/1000,instr.point[1]*5/1000]
    if position != Rx0:
        print('XY-stage lost its coordinates!!')
        instr.close()

# Moving Rx from Rx0 to the target position
def preload(instr,xy):
    instr.position()
    position = [instr.point[0]*5/1000,instr.point[1]*5/1000]
    if  position != Rx0:
        print('XY-stage lost its coordinates!!')
        instr.close()
    else:
        x = xy[0] - Rx0[0]
        y = xy[1] - Rx0[1]

        if y > 0:
            instr.moveUp(step = y, speed = Moving_speed)
            instr.moveRight(step = x, speed = Moving_speed)
        else:
            instr.moveRight(step = x, speed = Moving_speed)
            instr.moveUp(step = y, speed = Moving_speed)

def init(instr):
    instr.initialize(axis='XY')
    

# Move to the given Rx position
def moveTo(instr,Rx='Rx0'):
    Rx_now = check_position(instr)
    print(Rx_now)
    if Rx in Rxs.keys():
        if Rx_now == None:
            instr.close()
            print('Rx is not loaded on the mounting point!')
        elif Rx_now == Rx:
            print('Rx is loaded to point '+Rx_now+'!!!')
        else:
            print('1. picking up Rx.....')
            pickUp(instr)
            print(instr.point[0]*5/1000,instr.point[1]*5/1000)
            time.sleep(1)
            print('Move to Rx0...')
            move_to_Rx0(instr)
            print(instr.point[0]*5/1000,instr.point[1]*5/1000)
            time.sleep(1)
            print('Move to '+str(Rx)+' .....')
            preload(instr,Rxs[Rx])
            time.sleep(1)
            print('Load the Rx to '+str(Rx)+'...')
            load(instr)
            print('Rx is loaded to point '+Rx_now+'!!!')
    else:
        print('Please choose the Rx mounting position from ["Rx0","Rx1","Rx2","Rx3","Rx4"] !!')

def run(addr,RxNo='Rx0'):
    xy_stage = ISEL()
    xy_stage.connect(addr)
    if xy_stage.connection == True:
        print(RxNo)
        moveTo(xy_stage,Rx=RxNo)
        Rx_now = check_position(xy_stage)
        xy_stage.close()
        return Rx_now
    else:
        print('Can not build connection to XY-stage!!!')
        xy_stage.close()
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-RxNo', default='Rx0', help='Path to the input file')
    parser.add_argument('-addr', default='ASRL/dev/ttyUSB0::INSTR',action='store', help='XY_stage address.')
    parser.add_argument('-R',action='store_true',help='')
    parser.add_argument('-i',action='store_true',help='')
    parser.add_argument('-p',action='store_true',help='')
    
    args = parser.parse_args()
    
    #args.addr = 'ASRL/dev/ttyUSB0::INSTR'

    # Open interface of ISEL xy-stage
    XY_stage = ISEL()
    XY_stage.connect(args.addr)
    if XY_stage.connection == True:
        if args.i:
            XY_stage.initialize(axis='XY')
            XY_stage.move(Rx0,speed=[30,30])
            XY_stage.position()
            load(XY_stage)

        elif args.R:            
            #pickUp(XY_stage)
            moveTo(XY_stage,args.RxNo)
            print(np.array(XY_stage.point)*5/1000)
        elif args.p:
            print(check_position(XY_stage))
        XY_stage.close()
    else:
        print('Can not build connection to XY-stage!!!')
        XY_stage.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        







