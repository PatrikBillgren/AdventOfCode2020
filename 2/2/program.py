import re
p = '^(\d+)-(\d+) ([a-z]): ([a-z]+)$'
def condition(m):
    passw = m.group(4)
    return (passw[int(m.group(1)) - 1] == m.group(3)) != (passw[int(m.group(2)) - 1] == m.group(3))
print(sum(map(condition, [re.search(p, l) for l in open('i.txt')])))
