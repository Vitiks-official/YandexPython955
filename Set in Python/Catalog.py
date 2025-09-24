gusen = set()
for i in range(int(input())):
    vide = input()
    if vide in gusen:
        print("ДА")
    else:
        print("НЕТ")
    gusen.add(vide)