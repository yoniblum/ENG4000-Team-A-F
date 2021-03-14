
**System Configuration And Failure Tracking**

We are still waiting on some parts before implementing our design for the Beta release.
Once we get the parts we will assemble the design step by step and ensure that each component is working as required.
Initially we had planned on attaching a sensor to the Air-Preparation unit which would check if pressurised air was being received from the air compressor and 
being supplied to the solenoid valve, however, it’s cost was preventing us from meeting our budget constraints so we decided to exclude it for now. The pneumatic
cylinder we are using has 2 sensors mounted on it which check whether the piston is getting released and rectracted periodically. 

The sensors provide feedback to a Raspberry Pi which is also connected to a relay, which connects to a DC power supply. The Pi is also 
responsible for regulating power, we will alternate between 0 and 24V periodically (speed to be determined based on the pumping rate).
In case the sensors detect a fault/malfunction we will get notified by an LED lighting up through the Pi. In cases of failure/malfunction we will 
start by ensuring the solenoid valve which connects to the Pi is receiving power, if so we check to see if compressed air is being supplied to the pneumatic
cylinder everytime 24Vs is applied. If there was no fault in the connections of these components we will check whether the Air-Prep Unit is receiving compressed air
and forwarding it to the solenoid valve. If the solenoid valve is not getting compressed air, we must check and make sure the air filter is not clogged and the pressure 
regulator is set correctly. If there does not seem to be a problem with these components either we must ascertain the air compressor and reservoir are functional. 

These are the cautionary measures we are implementing in our design so that it could be troubleshooted seamlessly and efficiently. 
