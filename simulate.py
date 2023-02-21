from simulation import SIMULATION
# import pybullet as p
# import pybullet_data
# import time
# import pyrosim.pyrosim as pyrosim
# import numpy
# import math
# import random
# import constants as c


# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")


# p.loadSDF("world.sdf")

# pyrosim.Prepare_To_Simulate(robotId)

# backLegSensorValues = numpy.zeros(c.ITERATIONS)
# frontLegSensorValues = numpy.zeros(c.ITERATIONS)

# targetAngles_FrontLeg = c.amplitude_FrontLeg * numpy.sin(c.frequency_FrontLeg * numpy.linspace(0, 2*c.PI, c.ITERATIONS) + c.phaseOffset_FrontLeg)
# targetAngles_BackLeg = c.amplitude_BackLeg * numpy.sin(c.frequency_BackLeg * numpy.linspace(0, 2*c.PI, c.ITERATIONS) + c.phaseOffset_BackLeg)

# # Saving target angles to files for plotting
# # numpy.save("data/targetAngles_FrontLeg", targetAngles_FrontLeg)
# # numpy.save("data/targetAngles_BackLeg", targetAngles_BackLeg)
# # exit()

# for x in range(0,c.ITERATIONS):
#     p.stepSimulation()
#     time.sleep(1/60)

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
    
    

# numpy.save("data/backLegSensorValues", backLegSensorValues)
# numpy.save("data/frontLegSensorValues", frontLegSensorValues)

# p.disconnect()

simulation = SIMULATION()