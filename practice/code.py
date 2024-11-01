f = open("practice.in.txt")
for line in f:
    num = int(line)
    if num == 0:
        break

    if num % 2 == 0:
        print("The number " + line[:-1] + " is EVEN.")
    else:
        print("The number " + line[:-1] + " is ODD.")
