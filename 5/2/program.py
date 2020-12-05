lines = [line.rstrip('\n') for line in open('input')]
found = set(int(l.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2) for l in lines)
allSeats = set(range(894))
print(allSeats - found)
