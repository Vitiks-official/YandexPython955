max_speed_notviol = 0
was_viol = "НЕТ"
for i in range(int(input())):
    viol = False
    max_speed = 0
    for j in range(int(input())):
        speed = int(input())
        if speed > 60:
            viol = True
            was_viol = "ДА"
        if speed > max_speed:
            max_speed = speed
    if not viol and max_speed_notviol < max_speed:
        max_speed_notviol = max_speed
print(max_speed_notviol)
print(was_viol)