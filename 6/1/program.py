lines = open('input').read().split('\n\n')
print(sum(len(set(l.replace('\n', ''))) for l in lines))

