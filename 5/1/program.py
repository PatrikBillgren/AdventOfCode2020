lines = [line.rstrip('\n') for line in open('input')]
print(max(int(l.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2) for l in lines))
