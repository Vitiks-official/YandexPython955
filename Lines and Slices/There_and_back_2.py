line = input()
new_line = ""
for i in line:
    if i != " ":
        new_line += i
print(new_line == new_line[::-1])