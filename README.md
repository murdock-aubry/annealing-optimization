# Contents

- ``dist-opt.py``: Code for minimizing the distance between an arbitrary set of points in the real plane. The points of interest can either be inputted by the user, or randomly generated on a rectangular subdomain. 

- ``root_solver``: Code for finding the roots of a sufficiently nice function.


# Simulated Annealing

Simulated annealing is a Monte-Carlo random sample method for finding the global extremums of a function. This process has many applications in the world of optimization, and more specificially, solving for the *global* extremums. Other methods of numerical optimization, such as the gloden ratio search or gradient descent algorithms are optimal in situations where one is only interest in *local* extremum. 

Suppose that we have a physics system which reaches a state of equilibrium at some temperature $T$. Then it is well known that the Boltzmann probability distribution, which is given by

```math 
    P(E_j) = \frac{\exp(-\beta E_j)}{Z}
```

where 

```math
    Z = \sum_i \exp(-\beta E_i)
```

and $\beta = 1/k_BT$, provides the probability of the system being in a state $i$ at any given moment. Cooling the system by sending $T \to 0$, it follows that $\beta \to \infty$, and hence $\exp(\beta E_i)$ for all $i\neq 0$. In the case we are in the ground state, we have $\exp(\beta E_i) = 1$, immediately implying that $Z = 1$. Therefore, as $T \to 0$, the system must eventually fall into the ground state:

```math
    P(E_i) = \left\{\begin{aligned} &1  \ \ \ \mbox{for} \ \ E_i = 0 \\ &0 \ \ \ \mbox{else} \end{aligned} \right.
```
This approach can be applied to find the minimum of any functions $f(x_1, \ldots, x_n)$ by treating each point $\vec{x} \in \mathbb{R}^n$  as defining a state of the system.

We define the rate of cooling via the cooling parameter $\tau$, and set, at any time $t$;
```math
T = T_0\exp(t/\tau)
```
where $T_0$ is the initial temperature of the system.