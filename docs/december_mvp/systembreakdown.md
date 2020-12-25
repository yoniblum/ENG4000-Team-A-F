
<h1>Sprint Process -Team AF</h1>

Our Sprint Process included both long term and short term planning.  

The long term planning included deciding on the narrative for each of our two week sprints.  
These narratives encapsulated the primary goals of each sprint, which would move us forward to our minimum viable product, and eventually our final product.  These narratives were elected by our product owner, and validated by the group members.  

The “short term” planning consisted of two week sprints, which included seven meetings taking place on Mondays (x2) Wednesdays (x2) and Fridays (x2), and Sundays (x1).  

We had four types of meetings:

<h2>1. Sprint planning session </h2>
Before the meeting our product owner (Shivani) would populate the backlog with deliverables which would help the group fulfill the goal of our sprint narrative. These would be assigned story points according to the expected amount of time they would take to complete.  Before the meeting the product owner and the scrum master (Jonathan) would meet to refine the backlog.   During the meeting, these deliverables and their storypoint values would be adjusted democratically, and would be delegated to group members by the scrum master (Jonathan). The deliverables were delegated according to the skillset and availability of group members that week.  By the end of each sprint planning session, group members would depart with a strong sense of their sprint objectives/deliverables. 

<h2>2. Standup</h2>
<h2>The following link gives a description of the sprint planning: </h2>
<a href="https://github.com/SidB16/ENG4000-Team-A-F/blob/main/docs/gate1/sprint-planning.mdl"> SPRINT PLAN </a>

As we progressed the sprint process, our scrum master made a few adjustments with each iteration.  Namely, making the standups more discussion based, so that the group members would have a chance to question members while they did their standups.  This allowed group members to deliver feedback and suggestions to each other.  

<h2>3.  Meeting with project supervisor</h2>
The team would meet with Dr. Franz Newland, who would ensure our group was staying on track, and advise group members on how to achieve tasks.  These meetings consisted of updating Dr. Newland on our progress, and asking for advice on completing deliverables and improving our sprint planning. 

<h2>4. Sprint Review and Sprint Retrospective</h2>
This meeting would consist of a 30 minute sprint review which would aim to go over what we had achieved in our previous sprint, followed by a 30 minute retrospective in which we would go over how we could make each sprint iteration as optimal as possible.  

For the review, group members would update the other group members with what tasks they had accomplished that week, including the key takeaways for the rest of the group members. 
These reviews helped the scrum master determine how to run sprints more effectively.  For example, when group members were struggling to complete their tasks, it gave the scrum master an understanding of how to better incorporate workload into the delegation equation.  When a member   (Ie. how to allocate deliverables, populate backlog, manage workload, etc.  
 

For the retrospective, group members would populate a Stormboard (seen below) attached to our team AF Microsoft Teams channel.  This exercise would allow group members to discuss positive and negative aspects of the running of each sprint. We would conclude with a discussion on how we could improve our sprints.  These discussions were crucial for the product owner and scrum master to improve the sprints.  For example, in the storm board below, one member mentioned they wanted less “meetings lasting beyond the scheduled time”, since the members had meetings scheduled after some of the standups.  In response, the scrum master started creating schedules for each meeting, and made itineraries for each meeting according to what was the most urgent and essential.  




 



The schedule for our sprints were as follows:  

First Monday:<b> Sprint planning session + Standup</b>

First Wednesday: <b>Standup</b>
 
First Friday:  <b>Meeting with project supervisor </b>
Second Monday: <b>Standup</b>

Second Wednesday: <b>Standup</b>

Second Friday:  <b>Meeting with project supervisor</b>

Following Sunday: <b>Sprint Review and Sprint Retrospective</b>

Over the course of the semester we ran 3 sprints. 
The narratives were as follows:

1. Explore and Understand how BVM’s work 
(Specifications needed)

Our proprietary research had led us to conclude that an effective way to aid patients with breathing difficulties was by automating the pumping of an AMBU/BVM.  We had previously established that we would design automated BVM’s for ambulances in rural communities of Gujarat India, as it addressed a critical need for patients with breathing difficulties who were travelling long distances between hospitals.  

In order to understand how to do this effectively, it was crucial to acquire specifications for different BVM devices so we could develop a stronger understanding of what types of equipment we could use to meet our project requirements.  Additionally, we used our research to hone in on our design constraints and further develop our requirements. 

<b>Some key takeaways from this sprint: </b>
<ul>
<li>Group members developed a deep level of understanding of BVM’s, including understanding different BVM designs, including knowledge of the different components of BVM’s</li>
<li>Group members developed medical background of patient ventilation, including understanding appropriate applications and various implementations of the device ie. different settings for different oxygen levels, endotracheal intubation vs mask </li>
 <li>Modification of sprint: Itineraries included for each meeting</li>
     

<b>2. Explore possible design ideas for a crude pumping mechanism</b>

This sprint prepared the team for our end of semester goal of implementation of the crude pumping mechanism through an analysis of various pumping designs.  To evaluate pumping designs we developed criteria for pumping mechanisms.  We also developed as well as criteria for our system to be, which gave the group a stronger understanding of how close our MVP would be to our final design. Each group member researched a design idea for the mechanical “pumping” aspect of the Automated BVM, presented their research findings, and evaluated the pumping design based on criteria we had established at the beginning of the sprint.  

We ultimately decided that the most achievable design for our MVP would include converting a broken 3D printer into a pump, which would squeeze the BVM.   Although the group was happy with the research we had done in this sprint, we were a little anxious about falling behind on implementing the MVP. 

<b>Key takeaways from this sprint:</b> 
<ul>
 <li>Finalization of evaluation criteria for the pumping mechanisms for our BVM</li>
<li>Finalization of evaluation criteria for the system to be (following the MVP)</li>
 <li>Evaluation of various pumping mechanisms through an evaluation matrix</li>
<li>A design for a crude pumping mechanism (for the MVP)</li>
<li>Establishment of Hardware components to be used</li> 
<li>Following this sprint, we decided the research done in our sprints would be done concurrently with implementation</li>
</ul>
<b>3.Implement a crude pumping mechanism</b>

With our design prepared, the team got to work ordering parts and assembling the crude pumping mechanism.  The 3D printer we had been donated had built in stepper motors which could be controlled by Arduino Microcontrollers.  These stepper motors controlled a block which moved laterally.  With some modifications, and programming additions, we assembled and programmed the device to pump air at a rate of 14 pumps per minute, meeting our key design requirement.  

Since this sprint entailed implementation, rather than research, the team was faced with a few challenges.  First, determining how to effectively work on a hardware device, when the work had to be done remotely, and (due to budgetary restrictions), not all the group members had access to the parts.  Secondly, ordering parts during a time where walking into a hardware store was not possible.  These two challenges delayed our progress considerably and made it much more difficult to meet our design requirements. To overcome these challenges, we delegated tasks according to the abilities of each group member.  For example, group members with access to hardware components would work on assembly, and hardware configuration, while members without access would do research on additional components, and programming of existing components, which could be done remotely. We had a backup hardware design running in parallel with our main design as a contingency.  


 <b>Key takeaways from this sprint: </b>
<ul>
<li>An MVP device that met some of our design criteria</li>
<li>An understanding of how to effectively work remotely on hardware designs</li>
<li>An understanding of how to run concurrent processes such as research and implementation </li>
</ul>




