numbers = []

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break

    numbers.append(num)

for num in reversed(numbers):
    print(num)
