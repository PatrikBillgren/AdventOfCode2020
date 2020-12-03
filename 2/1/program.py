import re
p = '^(\d+)-(\d+) (.).*'
print(sum(map(lambda m: int(m[1]) <= m[0].count(m[3]) - 1 <= int(m[2]), [re.match(p, l) for l in open('i.txt')])))
