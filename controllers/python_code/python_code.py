from controller import Robot
from controller import Motor
from controller import Altimeter
from controller import LED
import math



class MyController(Robot):
    def __init__(self):
        super(MyController, self).__init__()
        self.timeStep = 32  # set the control time step

        # get device tags
        # self.distanceSensor = self.getDistanceSensor('my_distance_sensor')
        # self.led = self.getLed('my_led')
        # self.distanceSensor.enable(timeStep)  # enable sensors to read data from them
        
        self.altimeter=self.getDevice("altimeter")
        self.altimeter.enable(self.timeStep)
        
        self.left_motor = self.getDevice("left wheel motor")
        self.right_motor = self.getDevice("right wheel motor")
        self.left_motor.setPosition(math.inf)
        self.right_motor.setPosition(math.inf)
        self.direction_switch = False


    def run(self):
            
        while self.step(self.timeStep) != -1:
            # get the time step of the current world.
            
            altitude = self.altimeter.getValue()
            # print(altitude)
            if (not self.direction_switch):
                self.left_motor.setVelocity(2.0)
                self.right_motor.setVelocity(2.0)
                if (altitude <= 0.05):
                    self.direction_switch = True 
            else: 
                self.left_motor.setVelocity(-2.0)
                self.right_motor.setVelocity(-2.0)
                if (altitude >= 0.25):
                    self.direction_switch = False
    
# main Python program
controller = MyController()
controller.run()
