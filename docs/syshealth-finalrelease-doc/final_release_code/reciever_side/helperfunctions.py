import datetime
import json
import gspread
import boto3

#part3: get OAuth token to access google drive
gc = gspread.oauth() #try oauth
sns = boto3.client("sns", 
                   region_name="us-east-1", 
                   aws_access_key_id="*************************", 
                   aws_secret_access_key="*************************", 
                   aws_session_token="*************************")
    
def get_xbeeData_from_config_file(key_name):
    #open config file
    with open('config2.json') as config_file:
        data = json.load(config_file) 
    #get key_name from config file
    if key_name in data['xbeeData']:
        return data['xbeeData'][key_name]
    else:
        raise ValueError("Error: " + key_name + "value is not in config.json!")
def search_ambulanceID_from_config_file(xbeeMAC):
    #open config file
    with open('config2.json') as config_file:
        data = json.load(config_file)
    for keyval in data['ambulanceData']:
        if xbeeMAC.lower() == keyval['xbeeMAC'].lower():
            return keyval['ambulance']
def get_notificationData_from_config_file(key_name):
    #open config file
    with open('config2.json') as config_file:
        data = json.load(config_file) 
    #get key_name from config file
    if key_name in data['notificationData']:
        return data['notificationData'][key_name]
    else:
        raise ValueError("Error: " + key_name + "value is not in config.json!")
def data_receive_callback(xbee_message):
            #A) get the data from xbee, convert to String, and attach timestamp
            time = '%s' % datetime.datetime.now()
            message = str(xbee_message.data.decode())
            sender_MAC = str(xbee_message.remote_device.get_64bit_addr())

            #console logging
            print("From %s >> %s" % (sender_MAC, message))

            #open config file
            with open('config2.json') as config_file:
                data = json.load(config_file) 

            #B) validating incoming XBee's MAC, and reterving Ambulance ID from config file
            ambulanceID = search_ambulanceID_from_config_file(sender_MAC)
            if(ambulanceID != None):
                print("Ambulance ID is: " + ambulanceID)
            else:
                print("Ambulance ID not found")

            if (message == 'ERROR'):
                email = get_notificationData_from_config_file('email')
                cell = get_notificationData_from_config_file('cell')
                # Create SMS subscription
                response = sns.subscribe(TopicArn="arn:aws:sns:us-east-1:09277538165:myErrorNotification", Protocol="SMS", Endpoint="+1*********")
                subscription_arn = response["SubscriptionArn"]                


                # Create email subscription
                response = sns.subscribe(TopicArn="arn:aws:sns:us-east-1:09277538165:myErrorNotification", Protocol="email", Endpoint="sid16@my.yorku.ca")
                subscription_arn = response["SubscriptionArn"]

                # Publish to topic
                sns.publish(TopicArn="arn:aws:sns:us-east-1:09277538165:myErrorNotification", 
                            Message=message + " : " + time + " : " + ambulanceID, 
                            Subject="ERROR Encountered")

                # Send a single SMS (no topic, no subscription needed)
                sns.publish(PhoneNumber="+1*********", 
                Message="ERROR Encountered")
            
            #C) open, read and write to database
            sht = gc.open_by_url('https://docs.google.com/spreadsheets/d/1JBF7YKX42XMaTmYnoiCazo-XRLtaoHFikdbpw08NQ/edit?usp=sharing')
            worksheet = sht.worksheet("production-env")
            last_written_row = int(worksheet.cell(1,4).value)
            row = last_written_row + 1
            worksheet.update_cell(row, 1, ambulanceID)
            worksheet.update_cell(row, 2, message)
            worksheet.update_cell(row, 3, time)
            last_written_row = row
            worksheet.update_cell(1, 4, last_written_row)