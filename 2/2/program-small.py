import re
def check(line):
    m = re.search('^(\d+)-(\d+) ([a-z]): ([a-z]+)$', line) 
    return (m.group(4)[int(m.group(1)) - 1] == m.group(3)) != (m.group(4)[int(m.group(2)) - 1] == m.group(3))
print(sum(map(check, [line.rstrip('\n') for line in open('input')])))

