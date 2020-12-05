found = set(int(l.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2) for l in open('input'))
allSeats = set(range(894))
print(allSeats - found)
