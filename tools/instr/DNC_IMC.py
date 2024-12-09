#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import rs232
#import rs232
RS232=rs232.RS232
import numpy as np
import time
# rs232 constent
Timeout=1000;

# header of the xy setup
ISEL_CMD_INIT_XY='@03';
ISEL_CMD_REF='@0R'
ISEL_CMD_REF_SPEED='@0d'
ISEL_CMD_POS='@0P'
ISEL_CMD_VERSION='@0V'
ISEL_CMD_MOVE='@0M'
ISEL_NO_RESPONSE='Z'
#initialising controller parameters
ISEL_CMD_INIT_SPEED='@0Id'
ISEL_CMD_INIT_ACCEL='@0IJ'
ISEL_CMD_INIT_READ='@0IL'
ISEL_CMD_INIT_WRITE='@0IW'
ISEL_CMD_INIT_DEFAULT='@0IX'

# compile command
ISEL_CMD_CLEAR='@0k'
ISEL_CMD_START='@0i'
ISEL_CMD_END  ='9'

# 1.moving time setup
ISEL_MOVE_TIME=3000;
ISEL_REF_TIME=250000;
# 2 speed constent
ISEL_SPEED_MAX=10000;
ISEL_SPEED_MIN=100;
# 3. 
ISEL_X_MAX=230000;
ISEL_Y_MAX=210000;


# In[ ]:


'''1. #1define the ISEL xy stage commands'''
class ISEL(RS232):
    def __init__(self):
        RS232.__init__(self)
        self.check()
        self.point=['Nan','Nan']
        self.StartSpeed=100
        self.Acceleration=10
        self.RefSpeed=6000
        
    '''1. initialize '''
    def initialize(self,axis='XY'):
        if self.connection==True:
            #self.write_ascii('@0d6000,6000')
            #self.read_bytes(Max=1)
            self.write_ascii(ISEL_CMD_INIT_XY)
            self.read_bytes(Max=1)
            if axis=='XY':
                self.write_ascii(ISEL_CMD_REF+'3')
                print('xy')
                state=self.read_bytes(Max=1,Timeout=2*ISEL_REF_TIME)
                print(state)
                self.point=[0,0]
            if axis=='X':
                self.write_ascii(ISEL_CMD_REF+'1')
                state=self.read_bytes(Max=1,Timeout=ISEL_REF_TIME)
                self.point[0]=0
            if axis=='Y':
                self.write_ascii(ISEL_CMD_REF+'2')
                state=self.read_bytes(Max=1,Timeout=ISEL_REF_TIME)
                self.point[1]=0
            
    '''2. read current position'''
    def position(self, Timeout=5000):
        self.write_ascii(ISEL_CMD_POS)
        state=self.read_bytes(Timeout=Timeout)
        if state==b'0':
            x=int(self.read_bytes(Max=6),16)
            y=int(self.read_bytes(Max=6),16)
            z=int(self.read_bytes(Max=6),16)
            del z
            self.point[0]=float(x)
            self.point[1]=float(y)
        else:
            print('Error happens!')
            self.close()
        
    def move(self,position,speed=[100,100]):
        self.position()
        position[0]=int(position[0]*1000/5)
        position[1]=int(position[1]*1000/5)
        speed[0]=int(np.abs(speed[0])*1000/5)
        speed[1]=int(np.abs(speed[1])*1000/5)
        timeoutx=np.abs(self.point[0]-position[0])/(speed[0]+1)*1000
        timeouty=np.abs(self.point[1]-position[1])/(speed[1]+1)*1000
        timeout=int(timeoutx+timeouty+30000) 

        if position[0]<=int(1095*1000/5) and position[1]<=int(1095*1000/5):
            start=time.time()
            self.write_ascii('@0M '+str(position[0])+','+str(speed[0])+','+str(position[1])+','+str(speed[1]))
            state=self.read_bytes(Max=1,Timeout=timeout)
            t=(time.time()-start)
            self.position()
            return t
        else:
            print('The movement is out the limitation of xy-stage!')
            self.position(timeout=Timeout)
            return None
        
    def moveUp(self,step=10,speed=10):
        self.position()
        timeout=int(np.abs(np.abs(step)/speed)*1000+3000)
        step=int(step*1000/5)
        speed=int(speed*1000/5)
        if (self.point[0])<=int(1090*1000/5) and (self.point[1]+step)<=int(1090*1000/5):
            self.write_ascii('@0M '+str(self.point[0])+',500,'+str(self.point[1]+step)+','+str(speed))
            state=self.read_bytes(Max=1,Timeout=timeout)
            self.position()
        else:
            print('The movement is out the limitation of xy-stage!')
        
    def moveDown(self,step=10,speed=10):
        self.moveUp(step=-step,speed=speed)
        
    def moveRight(self,step=10,speed=10):
        self.position()
        timeout=int(np.abs(step/speed)*1000+3000)
        step=int(step*1000/5)
        speed=int(speed*1000/5)
        self.write_ascii('@0M '+str(self.point[0]+step)+','+str(speed)+','+str(self.point[1])+',500')
        state=self.read_bytes(Max=1,Timeout=timeout)
        self.position()
    
    def moveLeft(self,step=200,speed=500):
        self.moveRight(step=-step,speed=speed)
        
    # set default parameters
    def setStartSpeed(self,speed):
        # speed in units of Hz，300Hz=1500um/s
        self.write_ascii('@0j'+str(speed))
        self.read_bytes(Max=1)
        
    def setAcceleration(self,Acceleration):
        '''
        Acceleration =Hz/ms, 100Hz/ms=500um/s/ms=0.5mm/s/ms=500mm/s^2
        '''
        # set default acceleration
        self.write_ascii('@0J'+str(Acceleration))
        self.read_bytes(Max=1)    
    def setRefSpeed(self,RefSpeed):
        self.write_ascii(ISEL_CMD_REF_SPEED+str(RefSpeed))
        self.read_bytes(Max=1)

    '''function to compile the commands to the memory of ISEL'''
    def iserror(self):
        error=self.read_bytes(Max=1)
        print(error)
        state=False
        if error!=b'0':
            print('Error code:'+str(error))
            state=False
        else:
            state=True
        return state
    
    def Compile(self,commands):
        error={}
        # 1. clear the memory
        self.write_ascii(ISEL_CMD_CLEAR)
        state1=self.iserror()
        # 2. tell the instr to start writing commands
        self.write_ascii(ISEL_CMD_START)
        state2=self.iserror()
        state3=False
        state4=False
        if state1 and state2:
            for item in commands:
                self.write_ascii(item)
                state3=self.iserror()
                if state3==False:
                    break
        if state3 and (state1 and state2):
            self.write_ascii(ISEL_CMD_END)
            state4=self.iserror()
        if (state1 and state2) and (state3 and state4):
            print('the commands are compiled sucessfully!')
        else:
            print('error happens!')
 


        
    
        
        
        
            
            


 
