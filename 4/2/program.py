import re

height_p = 'hgt:(\d+)((cm|in))'
checks = [
        lambda x: re.search('byr:(\d{4})', x) is not None and 1920 <= int(re.search('byr:(\d{4})', x)[1]) <= 2002,
        lambda x: re.search('iyr:(\d{4})', x) is not None and 2010 <= int(re.search('iyr:(\d{4})', x)[1]) <= 2020,
        lambda x: re.search('eyr:(\d{4})', x) is not None and 2020 <= int(re.search('eyr:(\d{4})', x)[1]) <= 2030,
        lambda x: re.search(height_p, x) is not None \
            and (('cm' in re.search(height_p, x)[2] and 150 <= int(re.search(height_p, x)[1]) <= 193) \
            or ('in' in re.search(height_p, x)[2] and 59 <= int(re.search(height_p, x)[1]) <= 76)),
        lambda x: re.search('hcl:#([0-9a-f]{6})', x) is not None,
        lambda x: re.search('ecl:(amb|blu|brn|gry|grn|hzl|oth)', x) is not None,
        lambda x: re.search('pid:\d{9}(\D|$)', x) is not None,
        ]


print(sum(map(lambda s: all([f(s) for f in checks]), open('input').read().split('\n\n'))))

