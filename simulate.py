from simulation import SIMULATION
# import math
# import random
# import constants as c





# targetAngles_FrontLeg = c.amplitude_FrontLeg * numpy.sin(c.frequency_FrontLeg * numpy.linspace(0, 2*c.PI, c.ITERATIONS) + c.phaseOffset_FrontLeg)
# targetAngles_BackLeg = c.amplitude_BackLeg * numpy.sin(c.frequency_BackLeg * numpy.linspace(0, 2*c.PI, c.ITERATIONS) + c.phaseOffset_BackLeg)

# # Saving target angles to files for plotting
# # numpy.save("data/targetAngles_FrontLeg", targetAngles_FrontLeg)
# # numpy.save("data/targetAngles_BackLeg", targetAngles_BackLeg)
# # exit()


    

# numpy.save("data/backLegSensorValues", backLegSensorValues)
# numpy.save("data/frontLegSensorValues", frontLegSensorValues)


simulation = SIMULATION()
simulation.Run()

