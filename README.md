# An Autonomous Simultaneous Localization and Mapping Walker for Indoor Navigation

This project is part of the larger Parkinson's Disease research at NYIT. It extends to projects in fields of robotics, virtual reality, and gait tracking. The repository provides instructions and the source code for research paper: "Autonomous Simultaneous Localization and Mapping Walker for Indoor Navigation".

<img src="https://github.com/NYIT-PD/MoonWalker/blob/master/images/walker.png">


## Overview:
We propose an autonomous walker as a tool for the elderly and individuals with movement disorders who would benefit from additional support to maintain their balance and navigate from one place to another. The walker utilizes SLAM techniques using a LIDAR to map the environment the user is located in and voice commands to provide a friendly user interface to control the mapping of and navigation within the environment. The proposed walker autonomously navigates the user from one location to another while avoiding obstacles and detecting a possible fall of the user. We evaluated the walker system with AMCL, Gmapping, and Hector simultaneous localization and mapping techniques. Experiments were conducted in an indoor environment to examine the accuracy of the SLAM algorithms to an ideal path. The results show that AMCL achieves the lowest mean absolute error while navigating to its goal with an error of less of than 2.15% in terms of the total path distance. As future work, visual SLAM which uses computer vision to perform feature extraction and landmark identification and the inclusion of gait tracking capability for the walker can be considered to provide relevant data for personalized care.

## Requirements:

Clone this repository into the src folder of your catkin workspace using:

```
cd ~/catkin_ws/src

git clone https://github.com/pkashyap95/SLAM-Walker.git
```

## Hardware and Software Setup:
<p float="left">
<img src="https://github.com/NYIT-PD/MoonWalker/blob/master/images/hardware.png" width=350>
<img src="https://github.com/NYIT-PD/MoonWalker/blob/master/images/software.png" width=450 >
</p>

Above are Hardware (left) and Software (right) diagrams attached above.
