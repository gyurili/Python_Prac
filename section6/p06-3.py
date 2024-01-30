money = int(input("자판기에 얼마를 넣을까요? >>>"))

n = 1

while money >= 0:
    money -= 300

    if money >= 0:
        print("커피 {}잔 잔돈 {}원".format(n, money))
        n += 1
