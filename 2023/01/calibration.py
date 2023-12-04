with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

numbers = []

for line in lines:
    tmp = []
    for char in line:
        if char.isdigit():
            tmp.append(char)

    numbers.append(int(f"{tmp[0]}{tmp[-1]}"))

print(sum(numbers))