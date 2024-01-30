num1 = int(input("정수 1을 입력하세요: "))
num2 = int(input("정수 2을 입력하세요: "))
num3 = int(input("정수 3을 입력하세요: "))

if num1 > num2 and num1 > num3:
    print("가장 큰 수는 %d입니다." % num1)
elif num2 > num1 and num2 > num3:
    print("가장 큰 수는 %d입니다." % num2)
elif num3 > num1 and num3 > num2:
    print("가장 큰 수는 %d입니다." % num3)
