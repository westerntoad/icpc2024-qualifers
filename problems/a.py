import re

fileA = open("a.in.txt")
for line in fileA:
    if re.search(r".*[Bb].*[Rr].*[Aa].*[Ii].*[Nn].*[Ss].*", line):
        print("Tasty!")
    else:
        print("Not Tasty!")
