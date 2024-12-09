import urllib.request, json, requests
import time,datetime
import os,sys
import logging
import random
#
from astropy.coordinates import SkyCoord,EarthLocation,Angle
from astropy import units as u
from astropy.time import Time
#
from threading import Thread


logging.getLogger("requests").setLevel(logging.DEBUG)

def setup_logger(level):
  log_format = "%(asctime)s.%(msecs)03d :: %(levelname)s: %(filename)s - %(lineno)s - %(funcName)s()\t%(message)s" # with linenumber, functionname message               
  logging.basicConfig(format=log_format, level=level)
  log = logging.getLogger("python-tcs")
  log.info(f'logger setup with level {level}')
# check at system level

#
log_level =os.environ.get("LOGGING_LEVEL","INFO")
setup_logger(log_level)
log = logging.getLogger("python-tcs")

#
class telescope_control_system():
  def __init__(self,url):
    Thread.__init__(self)
    self.url = url
    self.log = logging.getLogger("python-tcs")
    self.log.info("setting up connection")
    # check status as ping test
    self.get_status()
    
  def post(self,cmd,data):
      if data=="":
        self.log.info(f'sending {self.url}{cmd}')
      else:
        self.log.info(f'sending {data} to {self.url}{cmd}')
      #
      try:
        response = requests.post(f'{self.url}{cmd}', data=json.dumps(data), allow_redirects=True)
        self.log.debug(f'response code: {response.status_code}')
      except requests.exceptions.RequestException as e:
            raise SystemExit(e)
      self.log.debug(f'{response.text}')
      if response.status_code == 503:
         self.log.warning(response.json().get("message",""))
         return {}
      if response.json().get("status","")=="error":
         self.log.error(response.json().get("message",""))
         sys.exit(-1)
      return response
      
  def get_status(self):
      cmd = "/acu/status"
      try:
        self.status = requests.get(self.url+cmd).json()
      except requests.exceptions.ConnectionError as e:
        self.log.error(f'failed to connect on {self.url} check is server up, exiting')
        sys.exit(-1)
      return(self.status)
        
  
  def abort(self):
      cmd="/abort"
      r = self.post(cmd,"")
      response = json.loads(r.content.decode())
      self.log.info(response)
      return response
      
      
  def track(self,coord:SkyCoord):
      start_dt = datetime.datetime.now() + datetime.timedelta(seconds=10)
      stop_dt = datetime.datetime.now() + datetime.timedelta(seconds=10e3)
      # azimuth scab example
      self.log.info(f'moving to {coord.ra},{coord.dec}')
      cmd = "/track"
      data ={
        "ra": coord.ra.deg,
        "dec": coord.dec.deg,
        "start_time": time.mktime(start_dt.timetuple()),
        "stop_time": time.mktime(stop_dt.timetuple()),
        "coordsys": "ICRS"
      }
      self.log.info(data)
      response = self.post(cmd,data)
      return response
  
  def move_to(self,azimuth:float,elevation:float):
      """
      send telescope to a given azimuth,elevation
      :param azimuth
      :param elevation
      """
      self.abort()
      time.sleep(2)
      # azimuth scab example
      cmd = "/move-to"
      data ={
        "azimuth": azimuth,
        "elevation": elevation
      }
      response = self.post(cmd,data)
      return response
  
  def azimuth_scan(self,start_time:float,elevation:float,azimuth_range:list,
                   num_scans:int,turnaround_time:float,speed:float):
      """
      send telescope on an azimuth scan at a constant elevation
      :start_time: time in future to begin scan, in format %Y-%m-%dT%H:%M:%SZ      
      :param elevation: elevation of telescope in deg
      :param azimuth_range: list with 2 floats containing range of azimuth 
      :param num_scan: numbers of cycles of the azimuth scan
      :turnaround_time: time to change scan direction in seconds
      :speed: speed of scan in degrees/second
      """
      # azimuth scab example
      cmd = "/azimuth-scan"
      data ={
        "azimuth_range": azimuth_range,
        "elevation": elevation,
        "num_scans": num_scans,
        "start_time": start_time,
        "turnaround_time": turnaround_time,
        "speed": speed
      }
      response = self.post(cmd,data)
      return response

  def scan_pattern(self,data):
       # track telescope
       dt = datetime.datetime.now() + datetime.timedelta(seconds=10)
       # azimuth scab example
       cmd = "/path"
       response = self.post(cmd, data=data)
       return response


if __name__=="__main__":
    tcs = telescope_control_system(url='http://127.0.0.1:5600')
    tcs.get_status()
    print(tcs.status)
    # track coord
    star_position = SkyCoord(140,30, unit=(u.deg,u.deg),frame="icrs")
    #response = tcs.track(star_position)
    # move to an az/ele
    #tcs.move_to(80.0,40.0)
    # azimuth_scan
    #azimuth_scan(elevation=60,azimuth_range=[110,130],num_scans=20,turnaround_time=30,speed=0.8)
    #tcs.azimuth_scan(self,float:elevation,list:azimuth_range,int:num_scans,int:turnaround_time,float:speed)
    #
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
    tcs.scan_pattern(data)
    while True:
       status = tcs.status
       log.info(f'{status["Elevation current position"]},{status["Azimuth current position"]}')
       time.sleep(1)
