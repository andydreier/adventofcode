with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

numbers = []

for line in lines:
    tmpNumbers = []
    for char in line:
        if char.isdigit():
            tmpNumbers.append(char)

    lineNumber = f"{tmpNumbers[0]}{tmpNumbers[-1]}"
    numbers.append(int(lineNumber))

# print(' '.join(numbers))
print(sum(numbers))