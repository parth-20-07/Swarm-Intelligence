**Assignment 3**

# Voting
Voting systems based on majority rule are susceptible to strategic agenda-setting. Let’s explore how one might do this on some basic examples.

Q.1) **Suppose there are four alternatives, named A, B, C, and D. There are three voters who have the following individual rankings:**

$B \succ_{1} C \succ_{1} D \succ_{1} A$

$C \succ_{2} D \succ_{2} A \succ_{2} B$

$D \succ_{3} A \succ_{3} B \succ_{3} C$


**You’re in charge of designing an agenda for considering the alternatives in pairs and eliminating them using majority vote, via an elimination tournament in the style of the examples shown in Slide 14 (at PDF page 19) of Lecture 11.**

The odds at this point are:
- $A \succ B$ --> Votes 2
- $B \succ C$ --> Votes 2
- $B \succ D$ --> Votes 2
- $C \succ A$ --> Votes 2
- $C \succ D$ --> Votes 2
- $D \succ A$ --> Votes 2

1. **You would like alternative A to win. Can you design an agenda (i.e., an elimination tournament) in which A wins? If so, describe how you would structure it; if not, explain why it is not possible.**

    A) To design an agenda in which alternative A wins, we can structure the tournament as follows:
    - Round 1: C (2V), D (1V) --> Winner: C
    - Round 2: B (2V), C (1V) --> Winner: B
    - Round 3: A (2V), B (1V) --> Winner: A

2. **You would like alternative B to win. Can you design an agenda (i.e., an elimination tournament) in which B wins? If so, describe how you would structure it; if not, explain why it is not possible.**

    A) To design an agenda in which alternative B wins, we can structure the tournament as follows:
    - Round 1: D (2V), A (1V) --> Winner: D
    - Round 2: C (2V), D (1V) --> Winner: C
    - Round 3: B (2V), C (1V) --> Winner: B

3. **You would like alternative C to win. Can you design an agenda (i.e., an elimination tournament) in which C wins? If so, describe how you would structure it; if not, explain why it is not possible.**

    A) To design an agenda in which alternative C wins, we can structure the tournament as follows:
    - Round 1: A (2V), B (1V) --> Winner: A
    - Round 2: D (2V), A (1V) --> Winner: D
    - Round 3: C (2V), D (1V) --> Winner: C

4. **You would like alternative D to win. Can you design an agenda (i.e., an elimination tournament) in which D wins? If so, describe how you would structure it; if not, explain why it is not possible.**

    A) To design an agenda in which alternative D wins, we can structure the tournament as follows:
    - Round 1: B (2V), C (1V) --> Winner: B
    - Round 2: A (2V), B (1V) --> Winner: A
    - Round 3: D (2V), A (1V) --> Winner: D

Q.2) **Now, consider the same question, but for a slightly different set of individual rankings in which the last two positions in voter 3’s ranking have been swapped. That is, we have:**

$B \succ_{1} C \succ_{1} D \succ_{1} A$

$C \succ_{2} D \succ_{2} A \succ_{2} B$

$D \succ_{3} A \succ_{3} C \succ_{3} B$



A) The odds at this point are:
- $A \succ B$ --> Votes 2
- $C \succ A$ --> Votes 2
- $C \succ B$ --> Votes 2
- $C \succ D$ --> Votes 2
- $D \succ A$ --> Votes 3
- $D \succ B$ --> Votes 2


1. **Can you design an agenda in which A wins? If so, describe how you would structure it; if not, explain why it is not possible.**

    A) Player A cannot win with the current odds. Round 3 needs Player A to win, So:
    - Round 3: A (2V), B (1V) --> Winner: A
        - Round 2: Not possible as B has no odds to win against any other player.
        
    Thus, there is no way for Player A to win.

2. **Can you design an agenda in which B wins? If so, describe how you would structure it; if not, explain why it is not possible.**

    A) Player B cannot win with the current odds. No match shows that it has odds to win against any other Rival.

3. **Can you design an agenda in which C wins? If so, describe how you would structure it; if not, explain why it is not possible.**

    A) To design an agenda in which alternative C wins, we can structure the tournament as follows:
    - Round 1: A (2V), B (1V) --> Winner: A
    - Round 2: D (3V), A (0V) --> Winner: D
    - Round 3: C (2V), D (1V) --> Winner: C
    
4. **Can you design an agenda in which D wins? If so, describe how you would structure it; if not, explain why it is not possible.**

    A) Player D cannot win with the current odds. Round 3 needs Player D to win, So, there are two options:
    - Round 3: D (3V), A (0V) --> Winner: D
        - Round 2: A (2V), B (1V) --> Winner: A
        - Round 1: Not possible as B has no odds to win against C
    - Round 3: D (2V), B (1V) --> Winner: D
        - Round 2: Not possible as B has no odds to win against C
        
    Thus, there is no way for Player D to win.

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