from itertools import count
from numpy import prod
paths = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
lines = [line.rstrip() for line in open('input')]
print(prod(list((sum(map(lambda x: x[1][x[0] % len(lines[0])] == '#', zip((count(start = path[0], step = path[0])), lines[path[1]::path[1]]))) for path in paths))))
