roomba_control

Controlling the behaviors of the roomba

HOW TO RUN

please add the following to your .bashrc
```
export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:~/catkin_ws/src/roomba_controls/models
```

If you were previously running the Gazebo-Ros sim please REMOVE the following from your .bashrc
```
export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:/home/eric/Computations/roomba_host/models
```



Assuming you have catkin, ROS kinetic, Gazebo, etc...

1. Open up a terminal and launch roscore
2. With roscore running, open another terminal.
3. Type . ~/catkin_ws/devel/setup.bash (you can probably make Linux do this automatically with the bash file but I'm not sure how to do that...)
4. Type  roslaunch roomba_control create_world.launch 
5. The sim should launch now. If it doesn't, please let me know!

# Roomba-Controls
#Roomba-Controls
