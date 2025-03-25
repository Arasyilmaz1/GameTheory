# GameTheory


Index Terms—Global Fibonacci Nim, Combinatorial Game
Theory, Deep Q Learning, Q Learning, Reinforcement Learning
Abstract—In 1997, an IBM super computer called Deep Blue
beat the world chess champion Garry Kasparov for the first
time in history. Since then, it has been a tradition for computer
scientists to create an engine to beat the best players on many
types of combinatorial games. In this paper, we continue this
tradition by using reinforcement learning approaches to find
a winning strategy for a variation of the game of Nim called
Global Fibonacci Nim. The optimal strategy for the game can be
recursively calculated in exponential time. However, Q Learning
algorithm improves the time complexity of the solution while
maintaining high accuracy. We use the optimal solution as a
benchmark for evaluating the performance of the agent.

I. INTRODUCTION
Combinatorial game theory is a field that lies at the inter-
section of mathematics and computer science [1], [2], [6]. It
utilizes concepts from abstract algebra as well as principles
from computer science, such as reinforcement learning. As
students majoring in mathematics and computer science, this
field offers an excellent opportunity to integrate our knowledge
from both disciplines and create a comprehensive and valuable
end product.
Given that Author 1 is conducting their mathematics cap-
stone on the theoretical research of this game, the algorithms
produced in this project are intended to support and enhance
this theoretical research. The primary goal of the project is to
design an agent capable of playing the game at a performance
level comparable to an optimal agent, especially in higher-
dimensional states. The processes and methods utilized in this
design may inspire similar applications in other types of games
and broader contexts.
To achieve this goal, we aim to deliver the following key
milestones:
1. A Python implementation of Q-Learning and Deep Q-
Learning algorithms for the game Global Fibonacci Nim.
2. A GUI user interface that allows users to play against
the trained agents.
3. A research paper demonstrating the correctness of the
algorithms, the optimization of agent hyper-parameters, and
an evaluation of agent performance.
4. A Python library for combinatorial game theory calcula-
tions, if time permits.

II. BACKGROUND
Combinatorial games are two-player games characterized
by the absence of hidden information and random chance
elements. Classic examples of such games include Nim and
Chomp. A run in a combinatorial game refers to a sequence
of alternating moves made by Player 1 and Player 2. Combina-
torial games are classified as short if they have a finite number
of distinct subpositions and do not permit infinite runs.
One notable example of a short combinatorial game is
Global Fibonacci Nim, which is governed by the specific rules
outlined below. Despite its potential for rich mathematical
exploration, this game has received limited attention in the
literature [4], [5].
Global Fibonacci Nim is played on N piles, each pile
having an arbitrary number of stones. There are two players
who take turns making moves. In the first turn, the player
selects one of the piles and removes as many stones as she
likes from the pile. In the next turns, players may remove up
to twice as many as the the number of stones removed in the
previous turn. The player who cannot make a move loses.
This game can be thought of as a combination of two other
combinatorial games: Nim and Fibonacci Nim. Understanding
these games and their winning strategies carries great impor-
tance for analyzing global Fibonacci nim. We now explain
these games.
Nim is played on n piles, each pile having arbitrary number
of stones. There are two players who take turns making moves.
In each turn, players select a pile and removes any number of
stones from that pile. The one who cannot make a move loses.
Fibonacci Nim is a variant of nim that is played on only one
pile. Two players take turns removing stones from that pile. In
the first turn, players can remove as many stones as they like,
but not all of it. In the next turns player may remove stones
up to twice as many as the stones removed on the previous
turn.

III. PROJECT OVERVIEW
In this section, we will review the subsections of the
research paper that we are going to produce. These sections
are:
1. Combinatorial Game Theory background
2. Global Fibonacci Nim Game
3. Optimal Play Algorithm
4. Implementing Q-Learning algorithm.
5. Implementing Deep Q Learning
6. Hyper-parameter Optimization
7. Evaluation of the performance of the agents.
8. Creation of the Combinatorial game theory API
9. Conclusion
Below is a more detailed explanation of the subsections.
A. Combinatorial Game Theory Background
This Section will include a summary of theoretical back-
ground of combinatorial games given in the book ’Combi-
natorial Game Theory’ by Aaron Siegel [6]. Also, important
terminology that is going to be used throughout the paper will
be given in this section.
B. Global Fibonacci Nim
This Section will describe and explain the ruleset of the
game together with a couple of sample plays. The state and
action space of the game will be described in this section.
C. Optimal Play Algorithm
This section will present the recursive algorithm for cal-
culating the outcome class for each state in the game. A
Discussion on the time complexity of the algorithm will be
held. The unfeasibility of the algorithm for high dimensional
state spaces will be explained. Improvements regarding the
algorithm will be discussed.
D. Q-Learning algorithm
An implementation of Q-Learning Algorithm for Global
Fibonacci Nim will be presented. Correctness of the Algorithm
will be discussed. The agent will be trained against multiple
opponents such as Optimal Player, Random Player, and Q-
Learning Player. The three parameters Alpha, Gamma, Epsilon
will be examined closely. Different agents will be trained using
different parameter values on the same number of games.
Statistical methods will be applied to decide on the better
learner.
E. Deep Q Learning
An implementation of Deep Q Learning Algorithm for the
game will be presented. The agent will be trained against mul-
tiple opponents such as Optimal Player, Random Player, and
Q-Learning Player. Different qualities of the neural network
that is used to update the Q Table will be discussed.
F. Hyper-Parameter Optimization
Hyper-parameters of the neural network and the parameters
of the Q-Learning will be optimized using Python libraries
such as Optuna. Different Agents trained on different condi-
tions will be compared.
G. Performance Evaluation
Performance of the Deep and Q Learning agents will
be evaluated using statistical methods and key performance
indicators. The best metrics to measure the performance will
be discussed. The evaluation of the agents will be made based
on the following criteria
1) Generalizability of the Performance to Different States
2) Time Consumption of the Agent
3) Largeness of the Training Pool
H. Combinatorial Game Theory Class
The comprehensiveness of this section can vary according
to the progress made in other sections by the stated deadline.
However, the goal of this section is to create a python library
that allows the mathematicians to make combinatorial game
computations. Although there is scripting language CGSuite
that does these calculations, no Python library corresponding
to this exists.

I. Conclusion
Significance of the results will be discussed both in the
context of computer science and mathematics. Further research
questions shall be generated. The ways in which Deep Q
learning algorithm improves upon the Optimal algorithm will
be stated. An example of how this algorithm can be used in the
search of solving Global Fibonacci Nim shall be demonstrated.

IV. TIMELINE AND TECHNOLOGY
In this section, we present the technology that will be used
in the project and the task division.
A. Technology
The project will be implemented in Python. We will use
Keras library for deep learning tasks, and Optuna for hyper-
parameter optimization. We might want to use scikit-learn
or Tensorflow instead, depending on the compatibility of the
library with our project. The paper will be written in IEEE
format.
B. Timeline
Table I includes the predicted task distribution and timeline
throughout block 7 distributed among the two authors. In
summary, Author 1 will be focusing on the mathematical
background while Author 2 will be more invested in the
coding aspect. Both Authors will be tackling the aspect of
implementing Machine Learning algorithms to solve the game.
