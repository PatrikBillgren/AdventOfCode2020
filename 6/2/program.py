from functools import reduce
lines = open('input').read().rstrip('\n').split('\n\n')
print(sum([len(reduce(lambda a,b: set(a).intersection(set(b)), l.split('\n'))) for l in lines]))
