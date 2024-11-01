

def problemA():
    fileA = open("a.in.txt")

    for line in fileA:
        brain = "brains"
        bIdx = 0
        for character in line:
            if bIdx == 6:
                break
            if character.lower() == brain[bIdx]:
                bIdx += 1

        if bIdx == 6:
            print("Tasty!")
        else:
            print("Not Tasty!")

def problemC():
    f = open("c.in.txt")
    lines = []
    for line in f:
        lines.append(line)

    idx = 0
    while True:
        if idx >= len(lines):
            break
        numLines = int(lines[idx])
        idx += 1
        ratios = []
        for i in range(numLines):
            values = lines[idx + i].split(" ")
            ratios.append(float(values[0]) / float(values[1]))
        
        ratios.sort()
        t = 1
        survived = True
        timeDied = 0
        for zombie in ratios:
            if zombie < t:
                survived = False
                timeDied = round(zombie, 1)
                break
            t += 1

        if survived:
            print("Survived.")
        else:
            print("Dead after " + str(timeDied) + " seconds.")
        idx += numLines

    


def problemD():
    f = open("d.in.txt")
    input = []
    for line in f:
        if line == "\n":
            dHelper(input)
            input = []
        else:
            input.append(line)


def dHelper(lines):
    wordMatrix = []
    for line in lines:
        line = line.replace(" \n", "")
        line = line.replace("\n", "")

        wordMatrix.append(line.split(" "))
    lines = wordMatrix



    y = 0
    x = 0
    if len(lines[0]) == 1:
        for line in lines:
            print(line[0])

    else:
        while y < len(lines):
            while x < len(lines[y]):
                if y >= len(lines[x]):
                    break
                print(lines[x][y] + " ", end="")
                x += 1
            print()
            x = 0
            y += 1
    print()





problemD()
