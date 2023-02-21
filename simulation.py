from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for x in range(0,c.ITERATIONS):
            print(x)
            p.stepSimulation()
            time.sleep(1/60)

        #     backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        #     frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

        #     pyrosim.Set_Motor_For_Joint(
        #         bodyIndex = robotId,
        #         jointName = "Torso_FrontLeg",
        #         controlMode = p.POSITION_CONTROL,
        #         targetPosition = targetAngles_FrontLeg[x],
        #         maxForce = c.MAX_FORCE)

        #     pyrosim.Set_Motor_For_Joint(
        #         bodyIndex = robotId,
        #         jointName = "Torso_BackLeg",
        #         controlMode = p.POSITION_CONTROL,
        #         targetPosition = targetAngles_BackLeg[x],
        #         maxForce = c.MAX_FORCE)
        
            
        