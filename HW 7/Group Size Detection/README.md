**Assignment 3: Group Size Detection**

**Table of Contents**
<!-- TOC -->

- [Introduction](#introduction)
    - [Install Dependencies](#install-dependencies)
- [Pseudocode](#pseudocode)
    - [How the files are structured](#how-the-files-are-structured)
        - [model.py](#modelpy)
        - [main.py](#mainpy)
    - [How to run the code](#how-to-run-the-code)
- [Results and Observations](#results-and-observations)
    - [Plot](#plot)
    - [Observations](#observations)
        - [Values of P and R that produce the best estimate](#values-of-p-and-r-that-produce-the-best-estimate)
        - [Does it matter if we use 4-distance or 8-distance?](#does-it-matter-if-we-use-4-distance-or-8-distance)
        - [Possible Improvement in the Algorithm](#possible-improvement-in-the-algorithm)
- [Resources](#resources)
- [Design Details](#design-details)
- [License](#license)

<!-- /TOC -->

# Introduction

Quorum sensing is **the regulation of gene expression in response to fluctuations in cell-population density**. Quorum-sensing bacteria produce and release chemical signal molecules called autoinducers that increase in concentration as a function of cell density.

![How Quorum Sensing Works](https://asm.org/ASM/media/Article-Images/2020/June/Quorum-sensing-500x500.jpg?ext=.jpg)

## Install Dependencies

Install all the essential Python dependencies[^1] using:

```sh
pip3 install -r requirements.txt
```

[^1]: *The complete code has been written on Ubuntu 20.04 LTS and not tested on any other system.*

# Pseudocode

```py
input:
    W = grid width [int]
    H = grid height [int]
    P = initiation probability [float]
    R = refractorytimer [int]

init:
    initiated = false [boolean]
    size = 0 [int]
    state = Susceptible

step:
    if (state == Susceptible)
        if (neighbor signalled)
            emit signal
            state = Refractory
            refractorytimer = R
            size = size + 1
        elif (not initiated) and (random() < P)
            emit signal
            state = Refractory
            refractorytimer = R
            initiated = true
            size = size + 1
        endif
    else
        refractorytimer = refractorytimer - 1
        if (refractorytimer <= 0)
            state = Susceptible
        endif
    endif
```

## How the files are structured

### model.py

The script contains the actual Group size detection model which takes the input:

- `width`: Grid Width (int: > 0)
- `height`: Grid Height (int: > 0)
- `probability`: Initiation Probability (P) (float: 0.01 - 1)
- `refractory_timer`: Number of steps before being susceptible again (P) (int: > 0)

### main.py

Contains a loop that imports the `model.py` file as a header and calls the model with different values of `width`, `height`, `P` and `R`.

## How to run the code

Open the terminal and run the code:

```sh
python3 main.py
```

# Results and Observations

## Plot

- `X-Axis`: Refractory Period (1 - 10)
- `Y-Axis`: Probability (0.01 - 1)
- `Z-Axis`: Max Grid Size

![Data Comparison](./Images/Graph.png)

## Observations

### Values of P and R that produce the best estimate

- For Estimated Value of M: 100, (R, P) pairs:
    - 0, 0.21
    - 0, 0.22
    - 0, 0.23
    - 0, 0.24
    - 0, 0.25
    - 1, 0.21
    - 1, 0.22
    - 1, 0.23
    - 1, 0.24
    - 1, 0.25
    - 2, 0.15
    - 2, 0.16
    - 3, 0.12
    - 4, 0.1
    - 5, 0.08
    - 6, 0.07
    - 7, 0.06
    - 9, 0.05

### Does it matter if we use 4-distance or 8-distance?
- 4 distance: 33 versions reached the size estimation of 100
- 8 distance: 16 versions reached the size estimation of 100

As the neighbors nearby are increased for flashing checks, the accuracy of the current rudimentary algorithm reduces.

### Possible Improvement in the Algorithm

- Improve the response of the grid by iterating through all neighbors to make immediate changes rather than waiting for the next iteration to happen.

# Resources

- [American Society for Microbiology: How Quorum Sensing Works](https://asm.org/Articles/2020/June/How-Quorum-Sensing-Works)

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