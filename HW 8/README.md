**Assignment 8**

**Table of Contents**

<!-- TOC -->

- [Introduction](#introduction)
- [Install Essentials](#install-essentials)
- [Robot Model](#robot-model)
    - [Proximity Sensor](#proximity-sensor)
    - [Range and Bearing Communication System](#range-and-bearing-communication-system)
- [Code](#code)
    - [Dispersion](#dispersion)
    - [Coupled Oscillation](#coupled-oscillation)
- [How to run the code](#how-to-run-the-code)
- [Simulation Results](#simulation-results)
    - [Starting Frame](#starting-frame)
- [Resources](#resources)

<!-- /TOC -->

# Introduction

The aim of the assignment is to simulation a swarm scenario where robots disperse around the environment while avoiding collisions and try to simulate coupled oscillations.

# Install Essentials

Three essential packages are needed to run this project:

- ARGoS (Swarm Simulation Software)
- Buzz (Programming Language for ARGoS)
- Khepera IV Robot (Robot used for simulation)

The complete installation guide can be found [here](./Docs/argos_buzz_installation.pdf).

# Robot Model

## Proximity Sensor

The proximity sensor on the robot is made up of 8 total sensors and numbered as follows.

![Robot](./Docs/Sensor.png)

## Range and Bearing Communication System

Range and Bearing Communication system is a feature in ARGoS where it connects and communicates with all the other robots in direct line of sight. Using this, it can communicate with its neighbors using publisher and subscriber network along with having the possibility to transmit position and orientation.

# Code

## Dispersion

```cpp
function go_to_random_location_while_avoiding_obstacles(){
    # Check if any front sensors are triggered. True -> Stop Robot, False -> Check for Rotation
    if((proximity[0].value > proximity_flag_val)&(proximity[1].value > proximity_flag_val)&(proximity[7].value > proximity_flag_val))
        gotop(0,0);

    # Check if front sensor is triggered. True -> Turn Right
    else if(proximity[0].value > proximity_flag_val)
        gotop(0,velocity_val);

    # Check if front left sensor is triggered. True -> Turn Right
    else if(proximity[1].value > proximity_flag_val)
        gotop(0,velocity_val);

    # Check if left sensor is triggered. True -> Turn Right
    else if(proximity[2].value > proximity_flag_val)
        gotop(0,velocity_val);

    # Check if front right sensor is triggered. True -> Turn Left
    else if(proximity[7].value > proximity_flag_val)
        gotop(0,-velocity_val);

    # Check if right sensor is triggered. True -> Turn Left
    else if(proximity[6].value > proximity_flag_val)
        gotop(0,-velocity_val);

    # Move Forward
    else
        gotop(velocity_val,0);
}
```

## Coupled Oscillation

Increment the `counter` and check if any neighbor flashed. If `c>=T`, flash light else don't.

```cpp
c = c+1;
neighbors.listen("flash", neighbor_flashed);
if(c>=T){
    set_leds(255,255,255);
    neighbors.broadcast("flash",true);
    c = 0;
}
else{
    set_leds(0,0,0);
}
```

Check `neighbor_flashed()` function

```cpp
function neighbor_flashed(){
    c = c+(k*c);
}
```

# How to run the code

Open the terminal and run the code:

```sh
argos3 -c hw8.argos
```

Two windows will pop up:

- ARGoS window
  ![ARGoS](./Docs/ARGoS.png)
- Buzz Editor
  ![Editor](./Docs/Buzz%20Editor.png)

Select `File->New/Open->hw8.bzz` to load the code script.

Press Execute (Gear Shaped Icon) to run the script.

Press Run in the ARGoS Window to start the simulation.

# Simulation Results

## Starting Frame

- The first initiated frame is shown below:
  
  ![First Frame](./Docs/Images/frame_0000000001.png)

- Simulation Video displaying Dispersion and Coupled Oscillation:

  ![Simulation](./Docs/animation.gif)

# Resources

- [Synchronization of Pulse-Coupled Biological Oscillators
  Renato E. Mirollo and Steven H. Strogatz
  SIAM Journal on Applied Mathematics 1990 50:6, 1645-1662](https://epubs.siam.org/doi/10.1137/0150098)
- [ARGoS Simulator](https://www.argos-sim.info/)
- [Buzz Wiki](https://the.swarming.buzz/wiki/doku.php?id=start)
