names = [input() for i in range(int(input()))]
for i in range(int(input())):
    name = input()
    if name in names:
        print(f"Вот твой подарок, {name}!")
        names.remove(name)
    else:
        print(f"{name}, всем по одному подарку!")