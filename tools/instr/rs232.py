#!/usr/bin/env python
# coding: utf-8
import pyvisa;
RS232_Timeout=5000;


def Device_check():
    rm=pyvisa.ResourceManager();
    Instr_item=[];
    for item in rm.list_resources():
        if 'ASRL' in item:
            Instr_item.append(item);
    
    return Instr_item;

''''''
class RS232():
    def __init__(self):
        # define the state constent
        self.connection=False;
        self.device_list=[];
        self.instr=None;
        self.rm=pyvisa.ResourceManager();
    def check(self):
        self.device_list=[];
        for item in self.rm.list_resources():
            if 'ASRL' in item:
                self.device_list.append(item);
        if self.device_list==[]:
            self.connection=False;
        
    def connect(self,device,baud_rate=19200):
        if device in self.rm.list_resources():
            self.instr=self.rm.open_resource(device);
            self.instr.read_termination='\r';
            self.instr.write_termination='\r';
            self.instr.timeout=RS232_Timeout;
            self.instr.baud_rate=baud_rate;
            self.connection=True;
            
        else:
            self.connection=False;
            
    def write_ascii(self,command):
        size_command=len(command)
        if self.connection:
            size=self.instr.write_ascii_values(command,[]);
            if size>=size_command:
                #print('All commands are sent sucessfully!');
                pass
            else:
                print('Error: Commands are not sent sucessfully!!');
        else:
            print('Error: please check the instrument connection!');
    
    def read_ascii(self,Timeout=RS232_Timeout):
        if(Timeout<0):
            #set the timeoutn to inf
            del self.instr.timeout
        else:
            self.instr.timeout=Timeout;
        string=self.instr.read_ascii_values();
        self.instr.timeout=RS232_Timeout;
        return string;
    
    def read_bytes(self,Max=1,Timeout=RS232_Timeout):
        if(Timeout<0):
            #set the timeoutn to inf
            del self.instr.timeout
        else:
            self.instr.timeout=Timeout;
        string=self.instr.read_bytes(Max);
        self.instr.timeout=RS232_Timeout;
        return string
    
    def close(self,):
        self.instr.close();
        self.connection=False;
            
                
        
        
