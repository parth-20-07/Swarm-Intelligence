**Assignment 3**

**Table of Contents**
<!-- TOC -->

- [Introduction](#introduction)
- [Code](#code)
    - [How the files are structured](#how-the-files-are-structured)
        - [requirements.txt](#requirementstxt)
        - [model.py](#modelpy)
        - [main.py](#mainpy)
    - [How to run the code](#how-to-run-the-code)
- [Results and Observations](#results-and-observations)
    - [Comparision Results](#comparision-results)
    - [How can fast segregation be reached?](#how-can-fast-segregation-be-reached)
    - [Interesting Experimentation](#interesting-experimentation)
    - [Individual Results](#individual-results)
- [Resources](#resources)

<!-- /TOC -->

# Introduction
Schelling's model of segregation is an agent-based model developed by economist Thomas Schelling. Schelling's work demonstrates that having people with "mild" in-group preference towards their own group could still lead to a highly segregated society via de facto segregation.

# Code

## How the files are structured

### requirements.txt

Contains the list of all the packages used in the project. The required packages can be installed by typing th following command:

```shell
pip install -r requirements.txt
```

### model.py

Contains the actual implementation of the **Schelling Model**. Due to the requirement of multiple tests, we do not run the code directly from this file. But you can run the code manually if needed as follows:

```shell
python3
```

This initiates a python instance in your terminal

```python
>>> import model
>>> model.schelling_model(0.6,4,False,1146)
```

### main.py

Contains the list of all the tests and implementations required for the assignment. Based on the requirements, the script is called by passing variables as required.

## How to run the code

Open the folder and launch a new terminal. Run the script using:

```shell
python3 main.py
```

:warning: *Be Aware: Loads of different variations are being tested, so the script will take about 10 - 12 minutes to fully execute depending on the performance of your computer!*

# Results and Observations

## Comparision Results

- 1D Coverage = 0.6

    ![0.6P,1D](/HW%203/Images/p61.png)

- 1D Coverage = 0.8

    ![0.8P,1D](/HW%203/Images/p81.png)

- 2D Coverage = 0.6

    ![0.8P,2D](/HW%203/Images/p62.png)

- 2D Coverage = 0.8

    ![0.8P,2D](/HW%203/Images/p82.png)

## How can fast segregation be reached?
- Fast Segregation can be reached by focusing on 1D Segregation where you focus on relocating on the same row for a new position.
- Segregation of **t = 4** can help proper collection of communities across a 2D Search. Trying to increase satisfaction level results into difficulty to achieve satisfaction for everyone.

## Interesting Experimentation
If we add the feature where we relocate the agent despite the required satisfaction level not achieved, but atleast better than its current state, we observe much better collection of agents in a clump. 

Though, this experimentation results in complete seperation of agents resulting into two seperate halves across the canvas.

## Individual Results

- 1D Coverage = 0.6, T = 3

    ![0.6P,T3](/HW%203/1D/Coverage%200.6/S%203/TS%201674794946/schelling_model.gif)

- 1D Coverage = 0.6, T = 4

    ![0.6P,T3](/HW%203/1D/Coverage%200.6/S%204/TS%201674794966/schelling_model.gif)

- 1D Coverage = 0.6, T = 5

    ![0.6P,T3](/HW%203/1D/Coverage%200.6/S%205/TS%201674795021/schelling_model.gif)

- 1D Coverage = 0.8, T = 3

    ![0.6P,T3](/HW%203/1D/Coverage%200.8/S%203/TS%201674795122/schelling_model.gif)

- 1D Coverage = 0.8, T = 4

    ![0.6P,T3](/HW%203/1D/Coverage%200.8/S%204/TS%201674795163/schelling_model.gif)

- 1D Coverage = 0.8, T = 5

    ![0.6P,T3](/HW%203/1D/Coverage%200.8/S%205/TS%201674795315/schelling_model.gif)

- 2D Coverage = 0.6, T = 3

    ![0.6P,T3](/HW%203/2D/Coverage%200.6/S%203/TS%201674795358/schelling_model.gif)

- 2D Coverage = 0.6, T = 4

    ![0.6P,T3](/HW%203/2D/Coverage%200.6/S%204/TS%201674795629/schelling_model.gif)

- 2D Coverage = 0.6, T = 5

    ![0.6P,T3](/HW%203/2D/Coverage%200.6/S%205/TS%201674796284/schelling_model.gif)

- 2D Coverage = 0.8, T = 3

    ![0.6P,T3](/HW%203/2D/Coverage%200.8/S%203/TS%201674796301/schelling_model.gif)

- 2D Coverage = 0.8, T = 4

    ![0.6P,T3](/HW%203/2D/Coverage%200.8/S%204/TS%201674796856/schelling_model.gif)

- 2D Coverage = 0.8, T = 5

    ![0.6P,T3](/HW%203/2D/Coverage%200.8/S%205/TS%201674797139/schelling_model.gif)


# Resources
- [Schelling's model of segregation
](https://en.wikipedia.org/wiki/Schelling%27s_model_of_segregation)