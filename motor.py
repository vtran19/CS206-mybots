import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.ITERATIONS)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.AMPLITUDE
        self.phaseOffset = c.PHASE_OFFSET
        self.frequency = c.FREQUENCY

        if self.jointName == "Torso_FrontLeg":
            self.motorValues = self.amplitude * numpy.sin(self.frequency/2 * numpy.linspace(0, 2*c.PI, c.ITERATIONS) + self.phaseOffset)
        else:
            self.motorValues = self.amplitude * numpy.sin(self.frequency * numpy.linspace(0, 2*c.PI, c.ITERATIONS) + self.phaseOffset)

    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = c.MAX_FORCE)

    def Save_Value(self):
        numpy.save("data/targetAngles_" + self.jointName, self.motorValues)
        