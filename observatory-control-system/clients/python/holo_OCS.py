# %%
import pytest
from astropy.coordinates import SkyCoord,EarthLocation,Angle
from astropy import units as u
import ocs
from ocs import observatory_control_system
import datetime,time
import random
import time
import copy
import random
import socket, struct

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.lines import Line2D

import argparse
# %%
def test_status():
  #
  ocs = observatory_control_system(url='https://127.0.0.1:5600',
                                   server_cert='../../tls/server.cert.pem',
                                   client_cert='../../tls/client.cert.pem',
                                   client_key='../../tls/client.key.pem')
  ocs.get_status()
  print('**************\n***************')
  for key in ocs.status.keys():
    print(key,':  ',ocs.status[key])
  #print(ocs.status)
# track coord

def test_track():
  ocs = observatory_control_system(url='https://127.0.0.1:5600',
                                   server_cert='../../tls/server.cert.pem',
                                   client_cert='../../tls/client.cert.pem',
                                   client_key='../../tls/client.key.pem')
  star_position = SkyCoord(140,30, unit=(u.deg,u.deg),frame="icrs")
  response = ocs.track(star_position)


def test_move():
  ocs = observatory_control_system(url='https://127.0.0.1:5600',
                                   server_cert='../../tls/server.cert.pem',
                                   client_cert='../../tls/client.cert.pem',
                                   client_key='../../tls/client.key.pem')
  # move to an az/ele
  ocs.move_to(80.0,40.0)
  #

  
def test_azi_scan():
  # azimuth_scan
  ocs = observatory_control_system(url='https://127.0.0.1:5600',
                                   server_cert='../../tls/server.cert.pem',
                                   client_cert='../../tls/client.cert.pem',
                                   client_key='../../tls/client.key.pem')
  start_dt = datetime.datetime.now() + datetime.timedelta(seconds=10)
  start_time = float(f'{time.mktime(start_dt.timetuple()):3.5f}')
  ocs.azimuth_scan(start_time,elevation=60,azimuth_range=[110,130],num_scans=20,turnaround_time=30,speed=0.8)
  
  
def test_path_horizon():
  # azimuth_scan
  ocs = observatory_control_system(url='https://127.0.0.1:5600',
                                   server_cert='../../tls/server.cert.pem',
                                   client_cert='../../tls/client.cert.pem',
                                   client_key='../../tls/client.key.pem')
  start_dt = datetime.datetime.now() + datetime.timedelta(seconds=10)
  data= {
    "start_time": float(f'{time.mktime(start_dt.timetuple()):3.5f}'),
    "coordsys": "Horizon",
    "points": [
        [0,   103+random.randint(0, 9), 50+random.randint(0, 9),0.5,0.5],
        [15,  106+random.randint(0, 9), 55+random.randint(0, 9),0.5,0.5],
        [30, 109+random.randint(0, 9), 60+random.randint(0, 9),0.5,0.5],
        [45, 112+random.randint(0, 9), 65+random.randint(0, 9),0.5,0.5]
    ]
  }
  #
  ocs.scan_pattern(data)


def test_position_broadcast():
    ocs = observatory_control_system(
        url="https://127.0.0.1:5600",
        server_cert="../../tls/server.cert.pem",
        client_cert="../../tls/client.cert.pem",
        client_key="../../tls/client.key.pem",
    )
    udp_host = "127.0.0.1"
    udp_port = 5601
    response = ocs.position_broadcast(udp_host, udp_port)
    print(response)
    # listen for data on host.name:5601 for ten cycles
    # setup udp socket and listen for data
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the host and port
    #sock.bind((udp_host, udp_port))
    print(f"Listening for UDP data on {udp_host}:{udp_port}")
    i = 0
    while i < 10:
        # Receive data from the socket
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        data_parsed = list(struct.unpack("<" + "".join(["Lddddddddd"] * 10), data))
        entries = [data_parsed[i : i + 10] for i in range(0, 100, 10)]
        print(f"Received message: {entries} from {addr}")
        i += 1

'''
Class for holo controlling system
'''
class holo_ocs_sys():
  def __init__(self,url='https://127.0.0.1:5600',
                    server_cert='../../tls/server.cert.pem',
                    client_cert='../../tls/client.cert.pem',
                    client_key='../../tls/client.key.pem'):
    
    self.url = url
    self.server_cert = server_cert
    self.client_cert = client_cert
    self.client_key = client_key
    self.ElData=[]
    self.AzData=[]
    self.t=[]
    self.vel=[]
    self.vaz=[]
    self.position=[0,0]
    self.velocity=[]
    
    self.t0 = None
    #self.open_ocs()
  def open_ocs(self):
    try:
      self.ocs = self.ocs = observatory_control_system(url=self.url,
                                    server_cert=self.server_cert,
                                    client_cert=self.client_cert,
                                    client_key=self.client_key)
      self.get_status()
    except:
      print('Cannot connect to FYST system remotely!!')


  def get_status(self):
    self.ocs.get_status()
    for key in self.ocs.status.keys():
      print(key,':  ',self.ocs.status[key])

  def get_position_velocity(self):
    self.ocs.get_status()
    self.position = [self.ocs.status['Elevation current position'],
                     self.ocs.status['Azimuth current position']]
    self.velocity = [self.ocs.status['Elevation current velocity'],
                     self.ocs.status['Azimuth current velocity']]
  def abort(self):
    response = self.ocs.abort()
    print('-------------------------')
    for key in response.keys():
      print(key,':  ',response[key])

  def move_to(self,Az,el):
    response = self.ocs.move_to(Az,el)
    #for key in response.keys():
    #  print(key,':  ',response[key])
    #print(response)

  def load_scan_pattern(self,filename):
    data = np.genfromtxt(filename)
    self.scan_points = data[0:10,0:5]
  
  def UDP_read(self,udp_host="127.0.0.1",udp_port=5601):
    response = self.ocs.position_broadcast(udp_host, udp_port)
    print(response)
    # listen for data on host.name:5601 for ten cycles
    # setup udp socket and listen for data
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    # Bind the socket to the host and port
    sock.bind(('', udp_port))
    print(f"Listening for UDP data on {udp_host}:{udp_port}")
    i = 0
    while i < 10:
      print(i)
      # Receive data from the socket
      #sock.listen(1)
      data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
      print("received message: %s"%data)
      data_parsed = list(struct.unpack("<" + "".join(["Lddddddddd"] * 10), data))
      entries = [data_parsed[n : n + 10] for n in range(0, 100, 10)]
      print(f"Received message: {entries} from {addr}")
      i += 1

  def start_scan(self, mapcenter=[10,3]):
    self.mapcenter = mapcenter
    scan_pattern = copy.copy(self.scan_points)
    scan_pattern[:,1:3] = self.scan_points[:,1:3] + np.array(mapcenter)
    self.abort()
    self.move_to(mapcenter[0],mapcenter[1])
    while True:
      self.get_position_velocity()
      print(self.position)
      if self.position == [mapcenter[1],mapcenter[0]]:
        break
      else:
        time.sleep(1)    
    self.get_position_velocity()
    start_dt = datetime.datetime.now() + datetime.timedelta(seconds=60)
    day_of_year = (start_dt - datetime.datetime(start_dt.year,1,1)).days + 1
    seconds_of_day = start_dt.hour*3600 + start_dt.minute*60 +start_dt.second + start_dt.microsecond/1000000
    self.t0 = day_of_year + seconds_of_day / (24*3600)
    data= {
      "start_time": float(f'{time.mktime(start_dt.timetuple()):3.5f}'),
      "coordsys": "Horizon",
      "points": scan_pattern.tolist()
    }

    self.ocs.scan_pattern(data)

  #### Mointering telescope scan pattern in real time. 
  def plot_update(self,data):
    t, point, velocity = data
    self.ElData.append(point[0])
    self.AzData.append(point[1])

    self.vel.append(velocity[0])
    self.vaz.append(velocity[1])
    
    with open(self.output_file,'a') as f:
      f.write(str(t)+','+str(point[1])+','+str(point[0])+','+str(velocity[1])+','+str(velocity[0])+'\n')
    self.trajectory.set_data(self.AzData, self.ElData)
    #self.ax0.set_xlim([self.mapcenter[0]-2,self.mapcenter[0]+2])
    #self.ax0.set_ylim([self.mapcenter[1]-2,self.mapcenter[1]+2])
    self.ax0.set_xlim([np.array(self.AzData).min()-2.5,np.array(self.AzData).max()+2.5])
    self.ax0.set_ylim([np.array(self.ElData).min()-0.5,np.array(self.ElData).max()+0.5])
    self.ax0.axis('equal')
    self.t.append(t)
    N=2000
    self.el_curve.set_data(self.t[-N:],self.ElData[-N:])
    self.vel_curve.set_data(self.t[-N:],self.vel[-N:])
    self.az_curve.set_data(self.t[-N:],self.AzData[-N:])
    self.vaz_curve.set_data(self.t[-N:],self.vaz[-N:])
    if t <= self.dT:
      self.ax1.set_xlim([0,self.dT])
      self.ax2.set_xlim([0,self.dT])
      self.ax3.set_xlim([0,self.dT])
      self.ax4.set_xlim([0,self.dT])
    else:
      self.ax1.set_xlim([t-self.dT,t])
      self.ax2.set_xlim([t-self.dT,t])
      self.ax3.set_xlim([t-self.dT,t])
      self.ax4.set_xlim([t-self.dT,t])

    self.ax1.set_ylim([np.array(self.ElData[-N:]).min()-0.2,np.array(self.ElData[-N:]).max()+0.2])
    self.ax2.set_ylim([np.array(self.AzData[-N:]).min()-0.2,np.array(self.AzData[-N:]).max()+0.2])
    self.ax3.set_ylim([np.array(self.vel[-N:]).min()-0.2,np.array(self.vel[-N:]).max()+0.2])    
    self.ax4.set_ylim([np.array(self.vaz[-N:]).min()-0.2,np.array(self.vaz[-N:]).max()+0.2])

    if t > 503.0:
      np.savetxt(self.output_file, np.concatenate((self.t,self.AzData,self.AzData,self.vaz,self.vel)).reshape(5,-1).T, delimiter=',')
    else:
      pass
    return self.trajectory#,self.el_curve
  
  def emitter(self):
    self.get_position_velocity()
    #t = (self.ocs.status['Time'] - self.t0)*24*3600
    t = self.ocs.status['Time']*24*3600 - self.t0
    yield t,self.position, self.velocity


  def pointing_mointer(self,plots=['trajectory','el','az','v_el','v_az'],
                       outputfilename='trajectory.dat'):
    self.output_file = outputfilename
    self.dT = 20
    self.ocs.get_status()
    if self.t0 == None:
      self.t0= self.ocs.status['Time']*24*3600
    else:
      pass

    fig = plt.figure(figsize=(7,15))
    '''create plotter to check telescope trajectory!'''
    fontsize=10
    labelsize=8
    self.ax0=plt.subplot(211)
    self.trajectory, = self.ax0.plot(self.AzData, self.ElData,'+-')
    self.ax0.set_xlabel('Az(Arcsec)',fontsize=fontsize)
    self.ax0.set_ylabel('El(Arcsec)',fontsize=fontsize)
    self.ax0.tick_params(axis='both', which='major', direction="in", labelsize=labelsize)

    self.ax1 = plt.subplot(425)
    self.el_curve, = self.ax1.plot(self.t,self.ElData,'b-')
    #self.ax1.set_xlabel('Time(s)',fontsize=fontsize)
    self.ax1.set_ylabel('El(Arcsec)',fontsize=fontsize)
    self.ax1.tick_params(axis='both', which='major', direction="in", labelsize=labelsize)
    
    self.ax2 = plt.subplot(426)
    self.az_curve, = self.ax2.plot(self.t,self.AzData,'g-')
    #self.ax2.set_xlabel('Time(s)',fontsize=fontsize)
    self.ax2.set_ylabel('Az(Arcsec)',fontsize=fontsize)
    self.ax2.yaxis.set_label_position('right')
    self.ax2.yaxis.tick_right()
    self.ax2.tick_params(axis='both', which='major', direction="in", labelsize=labelsize)
    
    self.ax3 = plt.subplot(427)
    self.vel_curve, = self.ax3.plot(self.t,self.vel,'-')
    self.ax3.set_xlabel('Time(s)',fontsize=fontsize)
    self.ax3.set_ylabel('V_El(Arcsec)',fontsize=fontsize)
    self.ax3.tick_params(axis='both', which='major', direction="in", labelsize=labelsize)

    self.ax4 = plt.subplot(428)
    self.vaz_curve, = self.ax4.plot(self.t,self.vaz,'-')
    self.ax4.set_xlabel('Time(s)',fontsize=fontsize)
    self.ax4.set_ylabel('V_Az(Arcsec)',fontsize=fontsize)
    self.ax4.yaxis.set_label_position('right')
    self.ax4.yaxis.tick_right()
    self.ax4.tick_params(axis='both', which='major', direction="in", labelsize=labelsize)

    ani = animation.FuncAnimation(fig, self.plot_update, self.emitter,interval=500,
                              blit=False)
    plt.show()


'''
animatation plots
'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', default='urs_scan_pattern/scan_50_minimal.dat',action='store', help='scan pattern file name.')
    parser.add_argument('-s',action='store_true',help='Load the scan pattern data and start the scanning.')
    parser.add_argument('-m', action='store_true', help='Mointering scan pattern')
    parser.add_argument('-o', default='trajectory.dat',action='store', help='Measured trajectory file.')

    args = parser.parse_args()
    print(args.f)
    print(args.m)
    Test = holo_ocs_sys()
    Test.open_ocs()
    Test.load_scan_pattern(args.f)
    #Test.move_to(10,10)
    #Test.UDP_read()
    if args.s:
      Test.abort()
      Test.start_scan()
      Test.UDP_read()
    if args.m:
      Test.pointing_mointer(outputfilename=args.o)
  
