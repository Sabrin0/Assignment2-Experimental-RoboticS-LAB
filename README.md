# Experimental Robotics LAB: Second Assignment

## Introduction 

The main purpose of this project is to update the [previous robot architecture](https://github.com/Sabrin0/Assignment1-Experimental-Robotics-LAB.git) in such a way that the different robot behaviors can be simulated in Gazebo. For this reason the FSM is quite similar to the previous one. It handles three states:

* **Normal**: in which the robot moves randomly, until the ball is reached
* **Sleep**: in which the robot reaches a predefined location and waits for some time
* **Play**: in which the robot tracks the green ball until it's still detected. Once it's next to the object it moves the head to check around.

As you can notice, the robots recalls the behavior of a dog so for this reason it's characterized by a main box chassis, two motorized wheels, one castor wheel, one cylinder neck and one head with one actuated degree of freedom. There is also a camera that, due to computer vision features, is able to detect a green ball.
(For more details, see the `urdf` directory).

## Software Architecture

![rosgraph](https://user-images.githubusercontent.com/73488155/102595642-36d6cf00-4118-11eb-95bb-c666e0637df0.png)

### Description

As mentioned in the above paragraph, this new software architecture still has a main node `cmd_man.py` which contains the FSM. This node due to the connection with the node `ballDetection.py` can check the current status (by subscribing to the topic `/robot/ballDetection`) in order to reach the desired statement.
In the meanwhile the action server `go_to_point_action.py` handles the robots movement, after it receives a goal from the FSM when the state *NORMAL* is active.

### parameters of interested and ROS messages

The ROS message `BallState.msg` stores two key parameters: 

* `BallDetected`: bool variable that is set to *true* whenever the ball is detected. After that, the FSM cancels the goal, stops the state *NORMAL* and returns the state *PLAY*.

* `currentRadius`: float that represents the radius of the current ball detected by the camera. When this value exceeds a defined threshold, we can assume that the ball is stopped and the robot is in front of it. So the robot stops and its head starts to rotate. Once the movement is finished the robot keeps tracking the ball.

The head movement is handled by the control framework *ros_control*, after the `cmd_man.py` publishes on the topic `/robot/joint_head_controller/command`. Instead, the robot movement is controlled by publishing on the topic `/robot/cmd_vel`.

## Package and file list 

Inside the directory `\src\exp_exprob2` all the main files are stored:

* *scripts*: where all the nodes are stored
* *msg*: where the message `BallState.msg` is defined
* *launch*: where the launch file is stored
* *urdf*: where the description of the complete environment is stored
* *config*: where the controller associated to the head is defined
 
## Installation and running procedure

First of all, in order to configure the ROS environment inside the current *workspace* the commands `catkin_make` is required as well as the sourcing of the setup.*sh files.
Then run:

```
$ roslaunch exp_assignment2 gazebo_world.launch

```
In this way several `[INFO]` are displayed, representing the current behavior of the state machine.
In order to test the architecture, in a new window run:

```
$ /reaching_goal/goal exp_assignment2/PlanningBallActionGoal "header:

```

In this way it's possible to control the ball movements by editing the *position* parameter. In details, by setting a negative value the **z** the ball will disappear and the FSM will exit from the *PLAY* state. 

## System Limitation and possible solutions

One of the biggest limitation is related to the robot movement. In particular when it's close to the ball its velocity is very slow, since the `BallDetection.py` provides a linear slowdown once the Ball is detected. So one possible solution is to improve the control loop feedback regarding the tracking. Moreover, when the robot is in the mode *NORMAL*, if the ball appears behind, it cannot enter in the mode *PLAY* until the mode *NORMAL* ends. This problem maybe can be overcome by implementing ambient sensor. Moreover, another test node can be run during the simulation in order to extend the robot visual:
 
```
$ rosrun exp_assignment2 head_control.py

```

### Contacts

Luca Covizzi 
luca@francocovizzi.it


