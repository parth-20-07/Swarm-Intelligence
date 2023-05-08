**Homework 9: Theraulaz Model**

**Table of Contents**

<!-- TOC -->

- [Introduction](#introduction)
- [Files](#files)
- [Simulation Parameters](#simulation-parameters)
- [Results and Observations](#results-and-observations)
- [Design Details](#design-details)
- [License](#license)

<!-- /TOC -->

# Introduction
The threshold model proposed by Theraulaz et al. is a mathematical model that explains how individual agents in a swarm determine their behavior based on the stimulus received from their environment and the behavior of other agents. The model assumes that each agent has a threshold value that determines its response to a particular stimulus. If the stimulus is below the threshold value, the agent ignores it, but if it exceeds the threshold value, the agent responds accordingly.

In Homework 9 Exercise 1, this model is implemented to study the specialization behavior of robots in a swarm. Each robot has a threshold value for two tasks, and the goal is to observe if robots specialize in one task or perform both tasks equally. The experiment records the behavior of each robot and analyzes the data to conclude the specialization behavior of the swarm.

# Files

**threshold_model.bzz**: Code to execute the threshold model.\
**plot.gp**: Code to plot the graphs.

# Simulation Parameters

- $\xi = 10$
- $\phi = 1$
- $p = 0.2$
- $dt = 20$
- Total Tasks = 2

# Results and Observations

![Graph](./Docs/Graph.png)

***Fig. Left: Task for a robot concerning Time***\
***Fig. Middle: Threshold 0 of robots concerning Time***\
***Fig. Right: Threshold 1 of robots concerning Time***


# Design Details
- Designed for:
  - Worcester Polytechnic Institute
  - RBE 595-S07 - ST: Swarm Intelligence Assignments
- Designed by:
  - [Parth Patel](mailto:parth.pmech@gmail.com)

# License

This project is licensed under [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) (see [LICENSE.md](LICENSE.md)).

Copyright 2023 Parth Patel

Licensed under the GNU General Public License, Version 3.0 (the "License"); you may not use this file except in compliance with the License.

You may obtain a copy of the License at

_https://www.gnu.org/licenses/gpl-3.0.en.html_

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.