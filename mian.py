# Define states and transitions matching the structure described in the report
states = {'q01', 'q02', 'q11', 'q12', 'q13', 'q14'}

system_moves = {
    ('q01', 'q01', 3), ('q01', 'q02', 4),
    ('q02', 'q01', 5), ('q02', 'q11', 6),
    ('q11', 'q11', 1),
    ('q12', 'q11', 6),
    ('q13', 'q11', 5),
    ('q14', 'q11', 7)
}

world_moves = {
    ('q01', 'q02', 4),
    ('q02', 'q01', 7), ('q02', 'q11', 5),
    ('q11', 'q12', 3),
    ('q12', 'q13', 2),
    ('q13', 'q11', 3), ('q13', 'q14', 2),
    ('q14', 'q11', 6)
}

# Run the minimization algorithm
relation, classes, reduced_system = weighted_alternating_simulation_minimization(states, system_moves, world_moves)

print("Equivalence Classes:", classes)
print("Reduced States (hat_S):", reduced_system[0])
print("Reduced System Moves:", reduced_system[1])