numbers = [int(line.rstrip('\n')) for line in open('input')]

for num1 in numbers:
    for num2 in (num for num in numbers if num1 + num == 2020):
        print(num1 * num2)


