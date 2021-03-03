### Page Index
- <small><i>Table of contents</i></small>
    + [About](#about)
    + [Architecture](#application-architecture)
    + [Configuration Management](#configuration-management)
    + [Testing](#testing)
    + [Appendix](#appendix)

### About Summary
Alpha release of a system health reporting application, utilizing XBee transceivers and Raspberry Pi3 to create a mesh network that uses peer-to-peer communication- visualizing and presenting the data transmitted within the nework as information, on a web-based dashboard.

### Background- What is this piece about and Why?
At of the start of the winter semester, our team decided to split into two-subteams. One dealing with the pump device, and the other dealing with failure reporting and visualizing system health. I took ownership of the latter.

In this part of the project, under the supervision of Professor.Franz Newland, I’m building a robust mechanism to collect health data of the automated BVM system. The end-goal is to share this data with the ambulance crew, and the base station personnel that monitor the health of the system.

### Product Vision- What is this piece of project doing?
This product is:
* Providing mechanism to report issues.
* Providing a low cost, mesh based communication. Allowing others abumblances to support a crew that might have fault.
* Provide a way to visualize data as gathered.

At the moment there is no automated reporting of device failures in an Ambulance operating in Gujarat, India. Thus, there is a need for automated failure reporting for mobile medical devices, used in various medical fields.

In essence, through this solution, the ambulance crew does not need to manually report/call-in a failure to the basestation personael.  
Furthermore, it allows one ambulance crew to support another, incase one experiences fault. The value is: if a automated BVM fails then a  higher load is placed on the crew, on top of pressure of caring for patients. This solutions minimizes the high workload placed on the ambulance crew- allowing them to focus on their patient. 

### Planned Releases
Beta Release- March 29th.
Final Release- April 12th.

### Application Architecture
<img src="gate4_syshealth_images/im1.png" alt=" " class="inline"/>

**Figure1 shows the architecture of the system health reporting application as of it's Alpha release.**

### Configuration Management
In this project, a Raspberry Pi 3 B+ and Dell Optiplex 7010 desktop are used as a the "ambulance" and "basestation", respectively. The key is transmission mode of the XBee transiver, to which the Pi or PC is connected too. Below I detail the hardware and software configuration of the Pi and the PC.

### Hardware
### Raspberry Pi 3 B+
<img src="gate4_syshealth_images/im5.png" alt=" " class="inline" width="400" height="400"/><br/>
Configuration(s):<br/>
Operating System:  Raspberry Pi OS 32-bit (Released: 2021-01-11, 1.1GB)<br/>
Manufacturer and Model: CanaKit, Raspberry Pi 3 Model B+<br/> 
Processor: Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC @ 1.4GHz<br/>
Python version: Python 3.6.9<br/>
Memory: 1GB LPDDR2 SDRAM<br/>
XBee Mode: Router<br/>
XBee Transport Mode: API 2<br/>
XBee Connection Port: /dev/ttyS0<br/>
XBee Baud Rate: 9600<br/>
XBee MAC address: 0013A2004125A5B9<br/>
Peripherals: 2.4Ghz "Ultra" Wifi dongle<br/>

Also, the below figure shows how the XBee is connected to the Raspberry Pi 3 B+:<br/>
<img src="gate4_syshealth_images/im7.png" alt=" " class="inline" width="400" height="400"/><br/>

### Basetation PC
<img src="gate4_syshealth_images/im6.png" alt=" " class="inline" width="400" height="400"/><br/>
Configuration(s):<br/>
Operating System:  Lubuntu 18.04<br/>
Manufacturer and Model: Dell, Optiplex 7010<br/>
Processor: 2.3 GHz Dual-Core Intel Core i5<br/>
Python version: Python 3.6.9<br/>
Memory: 8.0 GB<br/>
XBee Mode: Controller<br/>
XBee Transport Mode: API 2<br/>
XBee Connection Port: /dev/ttyUSB0<br/>
XBee Baud Rate: 115200<br/>
XBee MAC address: 0013A2004125A5B8<br/>

### Software 
### Raspberry Pi 3 B+
<img src="gate4_syshealth_images/im8.png" alt=" " class="inline"/>

### Basetation PC
<img src="gate4_syshealth_images/im9.png" alt=" " class="inline"/>

As of the Alpha release, software configurations are primarily minimal. However, towards the Beta release, configuration files will be created that contain code-based configurations in a single space- modulated away from data transmission source code. 

### Testing
### Testing the Mesh Network using XCTU
<img src="gate4_syshealth_images/im10.png" alt=" " class="inline" width="600" height="400"/>

### Testing Sending and Receving data using Python3
As of this Alpha release, a manual testing strategy is used. A Python3 script written on the sender side, and receiver side to send and receive data.

<img src="gate4_syshealth_images/im4.png" alt=" " class="inline" width="690" height="490"/>

**Figure4 shows how the Python3 scripts are used to test sending and receiving of data.**

### Results
This section contains three subsection that demonstrate the results of this Alpha Release. 

### 1) Raw Data Processed at the Basestation
<object data="https://docs.google.com/document/d/e/2PACX-1vS3oPCumTwzkfEPce57R6XSrqXaXSzlxlnErdOtRytYMSZzNwuyC5B_lHdbQMxnkSNnNaLHhbkhO4Y_/pub?embedded=true"  width="576" height="356" seamless frameborder="0" scrolling="no"></object>
**Figure5 shows the first build- version 1.0 where instead of generic database, a .txt file was used to store messages.**

### 2) Processed Data Visualized Real-time
<object data="https://docs.google.com/spreadsheets/d/e/2PACX-1vTOtlUA6_ut3XFsuj0FlkWg8S-ZV8Y1agQ2JxbpRSM8WFk134k7edO6xV-e-v02GFxi0yZMvwdY2nlV/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false" width="1000" height="500" seamless frameborder="0"></object>
**Figure6 shows the final build of the Alpha Release- data collected, processed and stored into a generic data-store on the Cloud. This spreadsheet is live. Please feel to scroll :)**

### 3) Data Presented Real-time
These two figures illustrate how the data collected can be visualized, and then presented on a website. This feature to embed visualizations will be used in the Beta release for better presentation of information.

<object data="https://docs.google.com/spreadsheets/d/e/2PACX-1vTOtlUA6_ut3XFsuj0FlkWg8S-ZV8Y1agQ2JxbpRSM8WFk134k7edO6xV-e-v02GFxi0yZMvwdY2nlV/pubchart?oid=2105202285&amp;format=interactive" width="576" height="356" seamless frameborder="0" scrolling="no"></object>
**Figure7 illustrates the System Status with respect to Time. This figure updates automatically as new database records are added.**

<object data="https://docs.google.com/spreadsheets/d/e/2PACX-1vTOtlUA6_ut3XFsuj0FlkWg8S-ZV8Y1agQ2JxbpRSM8WFk134k7edO6xV-e-v02GFxi0yZMvwdY2nlV/pubchart?oid=1815073469&amp;format=interactive" width="600" height="371" seamless frameborder="0" scrolling="no"></object>
**Figure8 illustrates Percentage of time Error and Ok states occurred. This figure updates automatically as new database records are added.**
