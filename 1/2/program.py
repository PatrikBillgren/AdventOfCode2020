numbers = [int(line.rstrip('\n')) for line in open('input')]

for num1 in numbers:
    for num2 in numbers:
        for num3 in numbers:
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)
                break


