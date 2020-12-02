import re
p = '^(\d+)-(\d+) ([a-z]): ([a-z]+)$'
print(sum(map(lambda m: int(m.group(1)) <= m.group(4).count(m.group(3)) <= int(m.group(2))
, [re.search(p, l) for l in open('i.txt')])))
