num = int(input("정수를 입력하세요: "))

if num < 0:
    print("잘못된 입력입니다.")

n = 1
while n <= num:
    print("%d번째 Hello" % n)
    n += 1
