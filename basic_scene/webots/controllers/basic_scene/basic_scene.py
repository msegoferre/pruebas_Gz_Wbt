"""basic_scene controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

import optparse
import math

# New library added so that we could measure time.
import time

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Create motor instances to control the wheels
left_front_wheel_motor = robot.getDevice('wheel1')
right_front_wheel_motor = robot.getDevice('wheel3')
left_rear_wheel_motor = robot.getDevice('wheel2')
right_rear_wheel_motor = robot.getDevice('wheel4')

# Set the target velocity for all wheels
target_velocity = 3.0  # Adjust this value as needed

left_front_wheel_motor.setPosition(float('inf'))  # Set the motor to velocity control mode
right_front_wheel_motor.setPosition(float('inf'))
left_rear_wheel_motor.setPosition(float('inf'))
right_rear_wheel_motor.setPosition(float('inf'))

left_front_wheel_motor.setVelocity(target_velocity)
right_front_wheel_motor.setVelocity(target_velocity)
left_rear_wheel_motor.setVelocity(target_velocity)
right_rear_wheel_motor.setVelocity(target_velocity)

# File where we're going to save FPS and RTF values
fps_rtf_log = open('rtf_fps_log.txt', 'w')
fps_rtf_log.write("Time (s), FPS, RTF\n")

# Time counter starts         
start_time = time.time()

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

    # FPS and RTF values are calculated
    current_time = time.time() - start_time
    fps = 1.0 / (time.time() - start_time)
    rtf = timestep / robot.getBasicTimeStep()

    # These values are written to the file 
    fps_rtf_log.write(f"{current_time:.2f}, {fps:.2f}, {rtf:.2f}\n")
    fps_rtf_log.flush()

    # Time counter is updated
    start_time = time.time()


# Close the log file
fps_rtf_log.close()

# Enter here exit cleanup code.
