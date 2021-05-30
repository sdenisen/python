s = open("output.txt", "w")
with open("input.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        a, b = l.split(" ")
        s.write(str(int(a) + int(b)) + "\n")

s.close()