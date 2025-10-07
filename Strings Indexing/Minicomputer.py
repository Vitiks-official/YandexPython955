line = input()
max_u = ord(line[0])
min_u = ord(line[0])
for i in set(line):
    if ord(i) > max_u:
        max_u = ord(i)
    if ord(i) < min_u:
        min_u = ord(i)
print(f"{min_u}, {max_u}")
print("ХВАТИТ" if len(set(line)) <= 32 else "НЕ ХВАТИТ")