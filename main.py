from random import randint
print("Добро пожаловать! В этой игре нужно проверять примеры. 1 - правильно, 2 - неправильно.")
run = True
while run:
    if randint(0, 1) == 1:
        bans = True
    else:
        bans = False
    s1 = randint(1, 99)
    s2 = randint(1, 90)
    if bans:
        ans = s1 + s2
    else:
        ans = randint(1, 198)
    print(f"{s1} + {s2} = {ans}?")
    pans = input(">>>")
    if pans == "1":
        pans = True
    else:
        pans = False
    if pans == bans:
        print("Правильно!")
    else:
        print("Неправильно!!!")
