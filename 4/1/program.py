lines = open('input').read().split('\n\n')
keys = ('byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:')
print(sum(map(lambda x: all([key in x for key in keys]), lines)))

