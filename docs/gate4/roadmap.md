
**Update on Roadmap:**

While in previous parts of our project we strictly adhered to the agile process, for our Alpha release, we pivoted to a more traditional waterfall style approach since we were determining which hardware we would be using in our final product: a process that is harder to do in an iterative manner. 

We started off in an agile fashion where we researched into our design aspects(pneumatic pumping and motor-driven design) and talked about the pros and cons with Michael Jenkins and Franz to narrow down our design scope.We were also trying to figure out the different  hardware components required for the automation, figuring out the microcontroller to use for each approach and trying to procure it if necessary and figure out the software control system for each approach.

We learned more about the capabilities of different mechanical systems and discussed the benefits and drawbacks of motor based designs and a pneumatic based designs and reaffirmed that a pneumatic design would be most suitable to meet our requirements for a few reasons. 



1. Better Meeting Technical Requirements- Pneumatic design wins over motor driven design in terms of providing more torque.
2. Noise Factor- The motor driven design produced a lot of noise but the pneumatic design is composed with silencer which numbs the sound.
3. Potential for longer periods of operation -One benefit of a pneumatic device is that it could operate for long periods of time as compared to electrical pumping mechanisms such as motors or linear actuators, which overheat with extended use.  

This design approach was further discussed with a senior engineer, Nimesh Joshi for his professional input. He walked us through the concept of pneumatic pumps and how we could situate the design in an ambulance. He also referred us to some mechanical/electronic component manufacturing companies that we could procure our pneumatic devices from.

Before ordering the parts from Festo,we checked to see if the 108 ambulances have an inbuilt compressor. We calculated the diameter of the self inflating bag and the stroke of the piston needed to pump the bag. Once we got the big picture, we contacted the application engineer who specializes in Festo products, Florin. He recommended the parts that would fit our [budget](https://github.com/SidB16/ENG4000-Team-A-F/blob/main/docs/gate4/Images/Billing/Q0542464%20(1).PDF), and would work well with our design. As soon as it was approved by the stakeholders, we started getting acquainted with Solidworks to model our Alpha design. For the Alpha release we have created a 3D model of our updated design using Solidworks whose snippets can be seen in our design section. We requested 3D solidworks part files for each Festo product which we assembled together using the [schematic](https://github.com/SidB16/ENG4000-Team-A-F/blob/main/docs/gate4/Images/schem.md).

We faced a number of challenges which slowed down our progress and it got harder to run our sprints. Firstly, communicating with stakeholders was difficult due to different time zones. Additionally, due to our project being mechanical and the remote nature of the course, it was difficult for us to adapt the agile approach that we had been using. We are using pneumatic design approach for our alpha release by making sure that all our previously mentioned requirements are taken into consideration



Followed by the alpha release, we have approved a plan with the help of stakeholders for how we wish to release our Beta and final release. For the Beta release we will be physically implementing the design, and testing each component and the system as a whole. Once we receive all the required parts, we will assemble it by following the above schematic. We will dive back into our agile project management process in which we will be researching how to obtain 0V and 24V signals from raspberry pi for the control of the 5/2-valve solenoid, and which  compressor to purchase for our design. Once we have all the physical components and the answers to our research questions we will assemble our design and implement it such that our software and hardware requirements are met.

For the Final Release, we will work on any unforeseen technical issues that were faced during the beta release, specified previously. We also plan on implementing a basic fault detection system to detect any loose connections between the components. 

s. 

