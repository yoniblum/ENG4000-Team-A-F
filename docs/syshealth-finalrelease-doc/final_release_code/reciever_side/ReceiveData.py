# SendData.py version
# Author: Siddharth Bhardwaj
# This script is running on the Basestation PC. It uses the Digi XBee library to recieve data that is sent in the mesh network,
# from the Router XBee (in the Ambulance).
#
# Version: 3.0- Final Release.
# Last Updated: March 29th, 2021  
#
# Below are libraries and helper functions imported. A seperate config.json file has been created to handle this program's configurations.

from digi.xbee.devices import XBeeDevice
from helperfunctions import get_xbeeData_from_config_file, data_receive_callback




def main():
    print(" +-----------------------------------------+")
    print(" |         XBee Listening for Data         |")
    print(" +-----------------------------------------+\n")
   
    #part1: load PORT and BAUD_RATE from config file to define local XBee connected
    PORT = get_xbeeData_from_config_file('port')
    BAUD_RATE = get_xbeeData_from_config_file('baud_rate')
    device = XBeeDevice(port=PORT, baud_rate=BAUD_RATE)
    try:
    #part2: open XBee connection
        device.open()
	#reading data does not block your application. Instead, you can be notified when new data has been received.
        device.add_data_received_callback(data_receive_callback) # calling function here!
        print("Waiting for data...\n")
        input()
    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()






