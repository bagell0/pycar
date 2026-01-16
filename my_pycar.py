from picarx import Picarx
from time import sleep
import sys
import tty
import termios
import select


class PyCar(Picarx):
    def __init__(self, servo=0, pan=0, tilt=0):
        super().__init__()
        
        #initial angles
        self.__servo0 = servo
        self.__pan0 = pan
        self.__tilt0 = tilt
        #direction angles
        self.servodir = servo
        self.pandir = pan
        self.tiltdir = tilt
        
        self.set_position()
        
        
        
    def set_position(self): #sets position to the direction angles
        self.set_dir_servo_angle(self.servodir)
        self.set_cam_pan_angle(self.pandir)
        self.set_cam_tilt_angle(self.tiltdir)
    
    def reset_position(self): #sets position to the initial angles
        self.set_dir_servo_angle(self.get_servo())
        self.set_cam_pan_angle(self.get_pan())
        self.set_cam_tilt_angle(self.get_tilt())
        
        
    def reset_dir(self, servo=None, pan=None, tilt=None):
        #sets the direction of the car to the specified direction (or initial)
        #kinda useless
        if servo is None:
            self.servodir = self.__servo0
        else:
            self.servodir = servo
        
        if pan is None:
            self.pandir = self.__pan0
        else:
            self.pandir = pan
        
        if tilt is None:
            self.tiltdir = self.__tilt0
        else:
            self.tiltdir = tilt
        
    def reset_angles(self): #resets memory initial angles
        self.set_servo(0)
        self.set_pan(0)
        self.set_tilt(0)
        
    #these fetch one of the angles (private attributes - that's why these methods exist)
    def get_servo(self):
        return self.__servo0
    def get_pan(self):
        return self.__pan0
    def get_tilt(self):
        return self.__tilt0
        
    #these set one of the stored angles to a specific value    
    def set_servo(self, servo):
        self.__servo0 = servo
    def set_pan(self, pan):
        self.__pan0 = pan
    def set_tilt(self, tilt):
        self.__tilt0 = tilt
        
    #turning methods
    def turn_left(self, step=2):
        self.servodir -= step
        self.set_position()
    def turn_right(self, step=2):
        self.servodir += step
        self.set_position()
    def pan_left(self, step=1):
        self.pandir -= step
        self.set_position()
    def pan_right(self, step=1):
        self.pandir += step
        self.set_position()
    def tilt_up(self, step=1):
        self.tiltdir += step
        self.set_position()
    def tild_down(self, step=1):
        self.tiltdir -= step
        self.set_position()
        
    #moving methods
    def fwd(self, speed=10, time=0.1):
        self.forward(speed)
        sleep(time)
    def bck(self, speed=10, time=0.1):
        self.backward(speed)
        sleep(time)
    
#The keyboard listener method. ChatGPT generated. I do not understand how it works
def get_key(timeout = 0.05):
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        if select.select([sys.stdin], [], [], timeout)[0]:
            return sys.stdin.read(1)
        return None
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

