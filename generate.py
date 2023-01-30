import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length, width, height = 1, 1, 1
x, y, z = 0, 0, 0.5

# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
# pyrosim.Send_Cube(name="Box2", pos=[x+1,y,z+1] , size=[length, width, height])

for row in range(5):
    length, width, height = 1, 1, 1
    for col in range(5):
        length, width, height = 1, 1, 1
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+row,y+col,z+i] , size=[length, width, height])
            length *= .90
            width *= .90
            height *= .90

pyrosim.End()
