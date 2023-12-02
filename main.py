import re
def readData(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def part1(fileName):
    lines = readData(fileName)
    totalIDs = 0
    for line in lines:
        idAndGame = line.split(":")
        id = int(idAndGame[0][5:])
        games = idAndGame[1].split(";")
        roundCount = True
        for game in games:
            rounds = game.split(",")
            for round in rounds:
                sanitizedRound=round.strip().split(" ")
                numCubes = int(sanitizedRound[0])
                if sanitizedRound[1][0] == 'b' and numCubes > 14:
                    roundCount = False
                elif sanitizedRound[1][0] == 'g' and numCubes > 13:
                    roundCount = False
                elif sanitizedRound[1][0] == 'r' and numCubes > 12:
                    roundCount = False
        if(roundCount):
            totalIDs += id
    print(totalIDs)

def part2(fileName):
    lines = readData(fileName)
    sumPowers = 0
    for line in lines:
        idAndGame = line.split(":")
        games = idAndGame[1].split(";")
        blueMax = 0
        greenMax = 0
        redMax = 0
        for game in games:
            rounds = game.split(",")
            for round in rounds:
                sanitizedRound=round.strip().split(" ")
                numCubes = int(sanitizedRound[0])
                if(sanitizedRound[1][0] == 'b' and numCubes > blueMax):
                    blueMax = numCubes
                elif sanitizedRound[1][0] == 'g' and numCubes > greenMax:
                    greenMax = numCubes
                elif sanitizedRound[1][0] == 'r' and numCubes > redMax:
                    redMax = numCubes
        power = blueMax * greenMax * redMax
        sumPowers += power
    print(sumPowers)




part2("day2input.txt")


