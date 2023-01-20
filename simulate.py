import pybullet as p
import time

physicsClient = p.connect(p.GUI)

for x in range(1001):
    time.sleep(1/60)
    p.stepSimulation()
    print(x)

p.disconnect()