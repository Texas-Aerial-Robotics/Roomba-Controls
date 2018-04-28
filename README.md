#roomba_control

Controlling the behaviors of the roomba

HOW TO RUN

please add the following to your .bashrc
```
export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:~/catkin_ws/src/roomba_controls/models
```

```
source ~/catkin_ws/devel/setup.bash
```
        
If you were previously running the Gazebo-Ros sim please REMOVE the following from your .bashrc
```
export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:/home/eric/Computations/roomba_host/models
```




Assuming you have catkin, ROS kinetic, Gazebo, etc...

1. Type . ~/catkin_ws/devel/setup.bash (skip this step if you sourced this in your .bashrc file)
2. Type  roslaunch roomba_control create_world.launch 
3. The sim should launch now. If it doesn't, please let me know!


