# Weighted Alternating Simulation Equivalence (ASE) Minimization

## Overview
This repository contains a Python implementation of a polynomial-time minimization algorithm for Weighted Labeled Transition Systems (WLTS) under Alternating Simulation Equivalence (ASE). The tool is designed for formal verification, reactive synthesis, and state-space reduction in two-player games (Controller vs. Environment) while preserving winning strategies and transition costs.

## Features
* **Maximal Simulation Relation:** Computes the greatest fixpoint simulation preorder respecting transition weight bounds for both system and environment moves.
* **Quotient Construction:** Automatically collapses mutually-simulating states into representative equivalence classes.
* **Game-Oriented Pruning:** Eliminates dominated controller choices and sub-optimal adversarial moves.
* **Inaccessible State Removal:** Cleans up unreachable states to yield a minimal graph unique up to isomorphism.

## Algorithm Steps
1. **Simulation Relation Computation:** Iteratively refines state pairs $(p, q)$ satisfying system and environment quantitative constraints.
2. **Equivalence Class Generation:** Groups states that mutually simulate each other.
3. **Reduced System Building:** Constructs the minimized transition system while mapping and preserving core cost structures.

## Usage
Import and execute the minimization function in Python by passing your state space, system moves, and world moves:

```python
from minimisation import weighted_alternating_simulation_minimization

# Define your states, system transitions, and world transitions
states = {'q01', 'q02', 'q11'}
system_moves = {('q01', 'q02', 4)}
world_moves = {('q02', 'q01', 5)}

relation, classes, reduced_system = weighted_alternating_simulation_minimization(states, system_moves, world_moves)