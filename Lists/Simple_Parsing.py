line = input()
lines = []
while line != "</html>":
    lines.append(line)
    line = input()
line = " ".join(lines)
answer = []
while "<p>" in line:
    answer.append(line[line.find("<p>") + 3:line.find("</p>")])
    line = line[line.find("</p>") + 4:]
print("\n".join(answer[::-1]))
