from collections import defaultdict

with open("input.txt", "r") as input_file:
    rawLines = input_file.readlines()


tmp = []

for i, rawLine in enumerate(rawLines):
    index = int(rawLine.split(":")[0].split(" ")[-1])
    games = rawLine.split(":")[-1].split(";")

    possible = True
    for j, game in enumerate(games):
        data = defaultdict(int)

        scores = game.strip().split(",")
        for score in scores:
            split = score.strip().split(" ")
            data[split[1]] += int(split[0])
        
        if data['red'] > 12 or data['green'] > 13 or data['blue'] > 14:
            possible = False
    

    if possible:
        tmp.append(index)

print(sum(tmp))

