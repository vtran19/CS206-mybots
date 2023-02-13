import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random

# Constants
PI = math.pi
ITERATIONS = 1000

amplitude_FrontLeg = PI/6
frequency_FrontLeg = 6
phaseOffset_FrontLeg = 0

amplitude_BackLeg = PI/8
frequency_BackLeg = 6
phaseOffset_BackLeg = PI/2

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")


p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(ITERATIONS)
frontLegSensorValues = numpy.zeros(ITERATIONS)

targetAngles_FrontLeg = amplitude_FrontLeg * numpy.sin(frequency_FrontLeg * numpy.linspace(0, 2*PI, ITERATIONS) + phaseOffset_FrontLeg)
targetAngles_BackLeg = amplitude_BackLeg * numpy.sin(frequency_BackLeg * numpy.linspace(0, 2*PI, ITERATIONS) + phaseOffset_BackLeg)

# Saving target angles to files for plotting
# numpy.save("data/targetAngles_FrontLeg", targetAngles_FrontLeg)
# numpy.save("data/targetAngles_BackLeg", targetAngles_BackLeg)
# exit()

for x in range(0,ITERATIONS):
    p.stepSimulation()
    time.sleep(1/60)

    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_FrontLeg[x],
        maxForce = 500)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_BackLeg[x],
        maxForce = 500)
    
    

numpy.save("data/backLegSensorValues", backLegSensorValues)
numpy.save("data/frontLegSensorValues", frontLegSensorValues)

p.disconnect()
