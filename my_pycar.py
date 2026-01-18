from picarx import Picarx
from time import sleep
import sys
import tty
import termios
import select


class PyCar(Picarx):
    
    DEFAULT_SPEED = 10
    DEFAULT_STEP = 2
    
    def __init__(self, servo_offset=0, pan_offset=0, tilt_offset=0):
        super().__init__()
        
        self.dir_servo_calibrate(servo_offset)
        self.cam_pan_servo_calibrate(-1*pan_offset)
        self.cam_tilt_servo_calibrate(-1*tilt_offset)
        
        #direction angles
        self.servodir = 0
        self.pandir = 0
        self.tiltdir = 0
        
        self.speed = self.DEFAULT_SPEED
        self.step = self.DEFAULT_STEP
        
        self.upd_dir()
        
        
        
    def upd_dir(self): #updates direction
        self.set_dir_servo_angle(self.servodir)
        self.set_cam_pan_angle(self.pandir)
        self.set_cam_tilt_angle(self.tiltdir)
    
    def set_neutral(self, cam=False): #direction goes neutral
        self.pandir = 0
        self.tiltdir = 0
        if cam: #if resetting just cam
            return 
        self.servodir = 0
            
    #directing methods
    def steer(self, right=False, left=False):
        if right and self.servodir < self.DIR_MAX:
            self.servodir += self.step
        if left and self.servodir > self.DIR_MIN:
            self.servodir -= self.step
        self.upd_dir()
    def pan(self, right=False, left=False):
        if right and self.pandir < self.CAM_PAN_MAX:
            self.pandir += self.step
        if left and self.pandir > self.CAM_PAN_MIN:
            self.pandir -= self.step
        self.upd_dir()
    def tilt(self, up=False, down=False):
        if up and self.tiltdir < self.CAM_TILT_MAX:
            self.tiltdir += self.step
        if down and self.tiltdir > self.CAM_TILT_MIN:
            self.tiltdir -= self.step
        self.upd_dir()
    
    #wrapper forward/backward methods
    def fwd(self):
        self.forward(self.speed)
    def bck(self):
        self.backward(self.speed)

