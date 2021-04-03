### Page Index
- [Technical Volume](#technical-volume)
  * [Executive Summary](#executive-summary)
  * [Product Vision](#product-vision)
  * [Solution Architecture](#solution-architecture)
    + [Architecture Diagram](#architecture-diagram)
    + [State Diagram](#state-diagram)
    + [Sequence Diagram](#sequence-diagram)
  * [System-As-Built Hardware](#system-as-built-hardware)
  * [System-As-Built Software](#system-as-built-software)
  * [Technical Demonstration Videos](#technical-demonstration-videos)
    + [Alpha Release](#alpha-release)
    + [Beta Release](#beta-release)
    + [Omega Release](#omega-release)
    + [Final Release](#final-release)
    + [Data Propogation Reliability Test](#data-propogation-reliability-test)
    + [Error Notification Feature](#error-notification-feature)
  * [Deep-dive into Code](#deep-dive-into-code)
- [Financial and Management Volume](#financial-and-management-volume)
   * [Backlog and Planned set of Deliveries](#backlog-and-planned-set-of-deliveries)
  * [Estimated Budget for Rebuild](#estimated-budget-for-rebuild)
  * [Business Plan](#business-plan)
  * [Failures and Lessons Learnt](#failures-and-lessons-learnt)
- [Appendix](#appendix)
  * [Video Transcripts](#video-transcripts)

## Technical Volume
### Executive Summary
Addresses: What is this project about and Why?

Final release of a solution that performs real-time analytics on the health of microcontroller systems in ambulance(s).

At the start of the winter semester, our team decided to split into two-subteams. One dealing with the pump device, and the other dealing with failure reporting and visualizing system health. I took ownership of the latter. (More information about the earlier phase of our project can be found [**here**](https://drive.google.com/file/d/1fbR2aad2eUqU_aILc2vjHCjWiD7Ffg1f/view?usp=sharing).) In this part of the project, under the supervision of Professor.Franz Newland, I’m building a robust mechanism to collect health data of the automated BVM system. The end-goal of this solution is to share this data real-time with the ambulance crew and base station personnel that monitor the health of the system.

In this solution, I create a mesh network of XBee transceivers to continuously send and recieve a Raspberry Pi's health data. Data on the mesh network is transmitted through peer-to-peer communication, and the microcontroller's health data is dependent on a real-time ouput from a gyroscopic sensor. (The gyroscope sensor simulates a automated Bag-Value-Mask (BVM) pumping mechanism in operation, inside of the ambulance). As system health data from the Pi is continuously transmitted, it is processed on a Basestation PC before being stored real-time onto a structured database, on the Cloud. As system health data is stored realtime, it presented realtime- as visuals on web-based analytics dashboard. A "open-source and free first" approach is used where Python3 and free Google services such as Google Spreadsheets and Google APIs (under a trial account) are used to implement a mechanism for data processing, data storage onto the Cloud, and data visualization on a stand-alone website.  

### Product Vision
Addresses: What is it doing?

This product is:
* Providing a mechanism to report issues.
* Providing a low cost, mesh based communication- allowing others abumblances to support a crew that might have fault.
* Providing a way to visualize data as gathered, real-time.
* Providing a way to push notifications to users if an issue is detected.
* Providing a way to configure the application during run-time, without stopping it.
* Providing a way to read health data from any type of pumping mechanism, using a gyroscopic sensor.

At the moment there is no automated reporting of device failures in an Ambulance operating in Gujarat, India. Thus, there is a need for automated failure reporting for mobile medical devices, used in various medical fields.

In essence, through this solution, the ambulance crew does not need to manually report/call-in a failure to the basestation personnel. Furthermore, it allows one ambulance crew to support another, incase one experiences fault. The value is: if a automated BVM unit fails then a higher load is placed on the crew, on top of pressure of caring for patients. This solution minimizes the high workload placed on the ambulance crew, allowing them to focus on their patients while providing a robust mechanism for reporting system failure. Furthermore, system health data that is collected realtime, is visualized realtime i.e. is leveraged to allow base station personnel to formulate a meaningful strategy to handle system failure (for example, re-route other active ambulances on the mesh network for support, incase one ambulance is experiencing fault with it's BVM).


### Solution Architecture
#### Architecture Diagram
<img src="syshealth-finalrelease-images/4k-architecture.png" alt=" " class="inline"/>
**Figure1** shows the end-to-end architecture of this application. It is also the highest-level view of this solution. Each phase of the solution is labelled (from 1 to 7), and a brief description is provided for each section. 

#### State Diagram
<img src="syshealth-finalrelease-images/4k_transition_sys.png" alt=" " class="inline"/>
**Figure2** shows the Alpha, Beta and (other) Omega releases in the form of a state diagram. This figure absracts away individual hardware and software components, considering them as a whole i.e. a system. A breif description about the state diagram, and each release is provided in the figure. For more information please refer to corresponding release(s) in the [Technical Video Demonstration section](#technical-demonstration-videos).

#### Sequence Diagram
<img src="syshealth-finalrelease-images/4k_sequence_diagram.png" alt=" " class="inline"/>
**Figure3** presents a lower-level view of this solution, compared to the architecture diagram. This figure considers the target user(s), and identifies their interaction with each component of the solution. In it, a Ambulance Crew or Basestation personnel memebers wants to view the dashboard. To do so they access the website, which is in production, and is updating the presentated analytics visuals; real-time as more microcontroller health data is transmitted (from the microcontroller in the ambulance, connected to an XBee transiever) and recieved on the Basestation.

### System-As-Built Hardware
##### Raspberry Pi 3 B+-- transmits health data
**Figure4** shows the fritzing diagram of microcontroller used in the the system-as-built, in this final release. It shows the Raspberry Pi B+ used, along with the XBee transiever and Gyroscopic sensor connected to it.<br/>
<img src="syshealth-finalrelease-images/4k_sender_circuit.png" alt=" " class="inline"/><br/>
Configuration(s):<br/>
Operating System:  Raspberry Pi OS 32-bit (Released: 2021-01-11, 1.1GB)<br/>
Manufacturer and Model: CanaKit, Raspberry Pi 3 Model B+<br/> 
Processor: Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC @ 1.4GHz<br/>
Python version: Python 3.6.9<br/>
Memory: 1GB LPDDR2 SDRAM<br/>
XBee Model: XBee Pro 538<br/>
XBee Mode: Router<br/>
XBee Transport Mode: API 2<br/>
XBee Connection Port: /dev/ttyS0<br/>
XBee Baud Rate: 9600<br/>
XBee MAC address: 0013A2004125A5B9<br/>
XCTU Version: 6.5.5<br/>
Gryoscope Sensor: MPU-6050 <br/>
Gryoscope Sensor Version: SEN-11028 <br/>

**Note**: XCTU was not installed on the Pi. This was because of software architecture constraints where XCTU executable code cannot run on a ARM based processor. <br/>

##### Basestation PC-- recieves health data
**Figure5** shows the fritzing diagram of Basestation PC used in the the system-as-built. It shows the chipset of my Desktop PC connected to the XBee transiever through a USB cord.<br/>
<img src="syshealth-finalrelease-images/4k_reciever_circuit.png" alt=" " class="inline" width="400" height="400"/><br/>
Configuration(s):<br/>
Operating System:  Lubuntu 18.04<br/>
Manufacturer and Model: Dell, Optiplex 7010<br/>
Processor: 2.3 GHz Dual-Core Intel Core i5<br/>
Python version: Python 3.6.9<br/>
Memory: 8.0 GB<br/>
XBee Model: XBee Pro 538<br/>
XBee Mode: Controller<br/>
XBee Transport Mode: API 2<br/>
XBee Connection Port: /dev/ttyUSB0<br/>
XBee Baud Rate: 115200<br/>
XBee MAC address: 0013A2004125A5B8<br/>

### System-As-Built Software
This ***[webapplication](http://webdashboard-env.eba-gddzrybt.us-east-1.elasticbeanstalk.com/)*** is the web-based, realtime system health reporting dashboard.<br/>
[![Final Release System Health Reporting Website](syshealth-finalrelease-images/4k_website_finalrelease.png)](http://webdashboard-env.eba-gddzrybt.us-east-1.elasticbeanstalk.com/ "Final Release Webapplication")

Brief explanation of code 🔨 🔨 🔨

### Technical Demonstration Videos
#### Alpha Release 
[![Alpha Release Demonstration Video](http://img.youtube.com/vi/JA0sFErDQJs/0.jpg)](http://www.youtube.com/watch?v=JA0sFErDQJs "Alpha Release")
##### Time Stamps
🔨 🔨 🔨

#### Beta Release 
[![Beta Release Demonstration Video](http://img.youtube.com/vi/hYYy9_IT4uc/0.jpg)](http://www.youtube.com/watch?v=hYYy9_IT4uc "Beta Release")
##### Time Stamps
🔨 🔨 🔨

#### Omega Release
[![Omega Release Demonstration Video](http://img.youtube.com/vi/XcdjYUXQX3U/0.jpg)](http://www.youtube.com/watch?v=XcdjYUXQX3U "Omega Release")
##### Time Stamps
🔨 🔨 🔨

#### Final Release 
🔨 🔨 🔨
##### Time Stamps
🔨 🔨 🔨

#### Data Propogation Reliability Test
[![Data Propogation Test Video Demonstration](http://img.youtube.com/vi/au7qQV5Tq-Q/0.jpg)](http://www.youtube.com/watch?v=au7qQV5Tq-Q "Data Propogation Reliability Test")
##### Time Stamps
🔨 🔨 🔨

#### Error Notification Feature
[![Error Notification Feature Demonstration](http://img.youtube.com/vi/tYvPlJ4o5VE/0.jpg)](http://www.youtube.com/watch?v=tYvPlJ4o5VE "Error Notification Feature")
##### Time Stamps
🔨 🔨 🔨

### Deep-dive into Code
🔨 🔨 🔨

## Financial and Management Volume
### Backlog and Planned set of Deliveries

### Estimated Budget for Rebuild

### Business Plan

### Failures and Lessons Learnt

## Appendix
### Video Transcripts
* [Alpha Release Video Transcript](video_transcripts/alpha_video_transcript.pdf)
* [Beta Release Video Transcript](video_transcripts/beta_video_transcript.pdf)
* [Omega Release Video Transcript](video_transcripts/omega_video_transcript.pdf)
* [Data Reliability Test Video Transcript](video_transcripts/omega_video_transcript.pdf)
* [Error Notification Feature Video Transcript](video_transcripts/errornotification_video_transcript.pdf)

## References
1. Deliverables Documentation.ENG4000 Fall-Winter-2020-21. Retrieved from: https://eclass.yorku.ca/eclass/course/view.php?id=6123

