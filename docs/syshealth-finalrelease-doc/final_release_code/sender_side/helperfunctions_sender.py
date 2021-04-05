import smbus
import math
import time
import json


with open('config_sender.json') as config_file:
        data = json.load(config_file)
bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = int(get_gyroData_from_config_file('address'), base=16) # This is the address value read via the i2cdetect command

def read_byte(adr):
	return bus.read_byte_data(address, adr)
 
def read_word(adr):
	high = bus.read_byte_data(address, adr)
	low = bus.read_byte_data(address, adr+1)
	val = (high << 8) + low
	return val
 
def read_word_2c(adr):
	val = read_word(adr)
	if (val >= 0x8000):
		return -((65535 - val) + 1)
	else:
		return val
 
def dist(a,b):
	return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
	radians = math.atan2(x, dist(y,z))
	return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
	radians = math.atan2(y, dist(x,z))
	return math.degrees(radians)

def get_xbeeData_from_config_file(key_name):
    #open config file
    with open('config_sender.json') as config_file:
        data = json.load(config_file) 
    #get key_name from config file
    if key_name in data['xbeeData']:
        return data['xbeeData'][key_name]
    else:
        raise ValueError("Error: " + key_name + "value is not in config.json!")

def get_gyroData_from_config_file(key_name):
    #open config file
    with open('config_sender.json') as config_file:
        data = json.load(config_file) 
    #get key_name from config file
    if key_name in data['gyroData']:
        return data['gyroData'][key_name]
    else:
        raise ValueError("Error: " + key_name + "value is not in config.json!")
