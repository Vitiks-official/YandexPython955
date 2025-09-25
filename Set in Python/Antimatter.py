line = "1"
all_pieces = set()
more2 = set()
current = set()
while line != "":
    line = input()
    current.add(line)
    if line == "-1":
        more2 = more2 | (all_pieces & current)
        all_pieces |= current
        current = set()
for i in all_pieces - more2:
    print(i, end=" ")