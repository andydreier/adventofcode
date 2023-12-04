with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

numbers = []

int_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for rawLine in lines:
    line = rawLine.strip().lower()
    tmp = []
    for i, char in enumerate(line):
        for value, name in enumerate(int_names):
            if name in line[i:i+len(name)]:
                tmp.append(value)
    
        if ord(char) <= 57:
            tmp.append(char)

    numbers.append(int(f"{tmp[0]}{tmp[-1]}"))

print(sum(numbers))