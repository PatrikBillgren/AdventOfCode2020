from itertools import count
lines = [line.rstrip() for line in open('input')]
print(sum(map(lambda x: x[1][x[0] % len(lines[0])] == '#', zip((count(start = 3, step = 3)), lines[1:]))))
