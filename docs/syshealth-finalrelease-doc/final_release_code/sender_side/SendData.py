# SendData.py version
# Author: Siddharth Bhardwaj
# This script is running on the Pi. It uses the Digi XBee library to send data to Controller XBee, on the mesh network.
#
# Version: 2.0- Final Release.
# Last Updated: March 29th, 2021 
#
# Below are libraries and helper functions imported. A seperate config_sender.json file has been created to handle this program's configurations.

from digi.xbee.devices import XBeeDevice #for interfacing with XBee
import smbus
import math
import time
import json
from helperfunctions_Sender import read_word_2c, get_xbeeData_from_config_file, get_gyroData_from_config_file

#XBee config
PORT = get_xbeeData_from_config_file('port')
BAUD_RATE = get_xbeeData_from_config_file('baud_rate')
REMOTE_NODE_ID = get_xbeeData_from_config_file('remote_node_id')

#Gyro Config
power_mgmt_1 = get_gyroData_from_config_file('power_management_register')
bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = get_gyroData_from_config_file('address') # This is the address value read via the i2cdetect command

def main():
    print(" +-----------------------------------------+")
    print(" |         XBee Sending Data         |")
    print(" +-----------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)
        
    try:
        # Now wake the 6050 up as it starts in sleep mode
        bus.write_byte_data(int(address, base=16), int(power_mgmt_1, base=16), 0)
	# Wake up XBee
        device.open()
        # Obtain the remote XBee device from the XBee network.
        xbee_network = device.get_network()
        remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
        if remote_device is None:
            print("Could not find the remote device")
            exit(1)
        while True:
            time.sleep(5) # pauses your Python program for 5seconds
            gyro_xout = read_word_2c(0x43) #anuglar velocity in x-axis
            gyro_yout = read_word_2c(0x45) #angular velocity in y-axis
            gyro_zout = read_word_2c(0x47) #angular velocity in z-axis
            
            # Pick DATA_TO_SEND
            x_threshold = int(get_gyroData_from_config_file('x_threshold'))
            y_threshold = int(get_gyroData_from_config_file('y_threshold'))
            z_threshold = int(get_gyroData_from_config_file('z_threshold'))

            if (gyro_xout > x_threshold and gyro_yout > y_threshold and gyro_zout > z_threshold):
                #use config file here to set threshold values through config
                DATA_TO_SEND = "OK"
            else:
                DATA_TO_SEND = "ERROR"

            print("Sending data to %s >> %s..." % (remote_device.get_64bit_addr(), DATA_TO_SEND))
            
            device.send_data(remote_device, DATA_TO_SEND)
            
            print("Success")
            
            time.sleep(5) # pauses your Python program for 5seconds

    finally:
        if device is not None and device.is_open():
            device.close()

if __name__ == '__main__':
    main()
    