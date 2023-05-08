**Assignment 2**

**Table of Contents**

<!-- TOC -->

- [Introduction](#introduction)
- [Triadic Closure](#triadic-closure)
- [Strong and Weak Ties](#strong-and-weak-ties)
- [Betweenness](#betweenness)
- [Design Details](#design-details)
- [License](#license)
- [Design Details](#design-details)
- [License](#license)

<!-- /TOC -->

# Introduction

The assignment aims to understand the networks by taking into account the human psychology and behavioral patterns observed.

**Networks** are collections of entities connected by the link.

**Graphs**

- **Graphs** are models of networks.
- A graph is a set of **nodes** connected by **edges**.
- Two nodes are **neighbors** if they are connected by one edge.

![Undirected Graph](./Images/Undirected%20Graph.png)

*(Fig. Undirected Graph)*

![Directed Graph](./Images/Directed%20Graph.png)

*(Fig. Directed Graph)*

# Triadic Closure

**Mark Granovetter** observed during his PdD that people while finding new jobs found new jobs from acquaintances, not close friends. For social networks,

*If two people in a social network have a friend in common, then there is an increased likelihood that they will become friends themselves at some point in the future.*

This principle is called **triadic closure**.

![Triadic Closure](./Images/Triadic%20Closure.png)

*(Fig. Triadic Closure)*

# Strong and Weak Ties

To make sense of Granovetter's findings, a new concept of the **strength** of an edge is introduced.
- A **strong Tie** corresponds to a close friendship.
- A **Weak Tie** corresponds to an acquaintance.

![Strong Weak Ties](./Images/Strong%20Weak%20Tie.png)

*(Fig. Strong/Weak Ties)*

If node **A** has edges to nodes **B** and **C**, then the **B−C** edge is **especially likely** to form if A’s edges to B and C are both **strong ties**.

# Betweenness

We define the **betweenness** of an edge to be the total amount of flow it carries, counting flow between all pairs of nodes using this edge.

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