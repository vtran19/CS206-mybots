from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c

class SIMULATION:
    def __init__(self, directOrGUI):
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
            c.SLEEP = 0
        else:
            self.physicsClient = p.connect(p.GUI)
            c.SLEEP = 1/60

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
    
    def __del__(self):
        p.disconnect()

    def Run(self):
        for timestep in range(0,c.ITERATIONS):
            p.stepSimulation()
            time.sleep(c.SLEEP)

            self.robot.Sense(timestep)
            self.robot.Think()
            self.robot.Act(timestep)
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()
        
            
        