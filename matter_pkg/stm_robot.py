from diagrama_clases_robot import *

from transitions import Machine, State

wallyActivity = Robot_Activity()

transitions = [
    { 'trigger': 'captura', 'source': 'found', 'dest': 'capturing' }
    ]

states = [
    State(name='found', on_exit=['say_goodbye']),
    'liquid',
    { 'name': 'capturing', 'on_enter': ['captura_img_obj']}
    ]

StateMachineRobot = Machine(model= wallyActivity, states=states, transitions=transitions, initial='found')

print(wallyActivity.state)

# El evento es captura

objeto_detectado = True
if (objeto_detectado):
    wallyActivity.captura()

print(wallyActivity.state)

