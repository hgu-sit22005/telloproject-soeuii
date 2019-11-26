from tello import Tello
import sys
from datetime import datetime
import time
import TelloPro

tello = Tello()

command_lst = []
command_lst.append(TelloPro.get_instance('takeoff', -1))
command_lst.append(TelloPro.get_instance('up', 100))
command_lst.append(TelloPro.get_instance('down', 50))
command_lst.append(TelloPro.get_instance('left', 50))
command_lst.append(TelloPro.get_instance('right', 50))
command_lst.append(TelloPro.get_instance('forward', 50))
command_lst.append(TelloPro.get_instance('back', 50))
command_lst.append(TelloPro.get_instance('cw', 45))
command_lst.append(TelloPro.get_instance('ccw', 45))
#for i in range(4):
#	command_lst.append(TelloPro.get_instance('flip', i))
command_lst.append(TelloPro.get_instance('land', -1))

for command in command_lst:
	tello.send_command_instance(command)