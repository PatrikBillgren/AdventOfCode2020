lines = [line.rstrip('\n') for line in open('input')]

count = 0

for line in lines:
    split = line.split()
    nums = split[0].split('-')
    mini = int(nums[0])
    maxi = int(nums[1])

    character = split[1][0]

    password = split[2]

    if (password[mini - 1] == character) != (password[maxi - 1] == character):
        count += 1
print(count)

