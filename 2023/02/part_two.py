from collections import defaultdict

with open("input.txt", "r") as input_file:
    rawLines = input_file.readlines()

result = 0

for i, rawLine in enumerate(rawLines):
    index = int(rawLine.split(":")[0].split(" ")[-1])
    games = rawLine.split(":")[-1].split(";")

    gameScores = defaultdict(list)
    for j, game in enumerate(games):
        
        scores = game.strip().split(",")
        for score in scores:
            split = score.strip().split(" ")
            gameScores[split[1]].append(int(split[0]))

    result += max(gameScores['red']) * max(gameScores['green']) * max(gameScores['blue'])

print(result)
