from transitions import Machine
import matplotlib.pyplot as plt
from test import *
#from matter_pkg.test import suma
from nature import *

protomolecula = Matter()

# Voy a usar la siguiente biblioteca https://github.com/pytransitions/transitions

#crear una maquina de estado para el modelo de protomolecula
#suegerido por la biblioteca
states = ['solid', 'liquid', 'gas', 'plasma']

#create transitions
transitions = [{ 'trigger': 'melt', 'source': 'solid', 'dest': 'liquid' },
    { 'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas' },
    { 'trigger': 'sublimate', 'source': 'solid', 'dest': 'gas' },
    { 'trigger': 'ionize', 'source': 'gas', 'dest': 'plasma' }
]

#initialize the model
stateMachineMatter = Machine(model=protomolecula, states=states, transitions=transitions, initial='solid')



#test
print(protomolecula.state)
protomolecula.melt()
print(protomolecula.state)

#test
print(protomolecula.state)
protomolecula.evaporate()
print(protomolecula.state)


