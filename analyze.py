import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetAngles_FrontLeg = numpy.load("data/targetAngles_FrontLeg.npy")
targetAngles_BackLeg = numpy.load("data/targetAngles_BackLeg.npy")

# matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=4)
# matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg")
matplotlib.pyplot.plot(targetAngles_FrontLeg, label="Front Leg Target", linewidth=4)
matplotlib.pyplot.plot(targetAngles_BackLeg, label="Back Leg Target")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

