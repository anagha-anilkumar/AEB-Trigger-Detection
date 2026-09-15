1. Project Overview

This project implements an Automatic Emergency Braking (AEB) trigger detection system using vehicle telemetry data.

The program reads a CSV file containing:

- timestamp
- speed
- obstacle_distance

It calculates the Time To Collision (TTC) and determines whether emergency braking should be triggered.

According to the MOTOREX task requirement:

> AEB is triggered when the Time To Collision (TTC) is less than 2 seconds.


2. Objectives

The program performs the following tasks:

1. Load vehicle telemetry data from a CSV file.
2. Calculate Time To Collision (TTC).
3. Add an `emergency_brake` column containing `0` or `1`.
4. Count the number of separate AEB events.
5. Find the closest detected obstacle.
6. Display the results in the terminal.
7. Save the processed data as a new CSV file.



3. Input Data

The input CSV file is:

vehicle_sensor_data.csv

It contains the following columns:

|       Column        |     Description      |   Unit  |
|---------------------|----------------------|---------|
|     `timestamp`     |  Time of measurement | seconds |
|        `speed`      |    Vehicle speed     |  m/s    |
| `obstacle_distance` | Distance to obstacle |  metres |

The speed unit was confirmed by the MOTOREX organizers as **m/s**.



4. Time To Collision (TTC)

The Time To Collision is calculated using:

text
TTC = obstacle_distance / speed
