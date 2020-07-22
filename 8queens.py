#!/usr/bin/python3
from itertools import permutations

solutions = []

columns = range(8)
for perm in permutations(columns):
    diag1 = set()
    diag2 = set()
    for i in columns:
        diag1.add(perm[i]+i) # checks / diagonal
        diag2.add(perm[i]-i) # checks \ diagonal
    if 8 == len(diag1) == len(diag2):
        solutions.append(perm)

for sol in solutions:
    print (sol)
