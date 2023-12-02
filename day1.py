from word2number import w2n

def readData(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines

def calibrateDocument(fileName):
    lines = readData(fileName)
    print(lines)
    firstNumber = -1;
    secondNumber = -1;
    total = 0;
    for line in lines:
        line = (line.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine"))
        for character in line:
            if character.isdigit() and firstNumber == -1:
                firstNumber = character;
            elif character.isdigit():
                secondNumber = character;
        if(secondNumber == -1):
            secondNumber = firstNumber
        total += int(firstNumber) * 10 + int(secondNumber)
        firstNumber = -1
        secondNumber = -1
    print("Total is " + str(total))

calibrateDocument("day1input.txt")


