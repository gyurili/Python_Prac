num1 = int(input("국어 점수를 입력하세요: "))
num2 = int(input("영어 점수를 입력하세요: "))
num3 = int(input("수학 점수를 입력하세요: "))

res = (num1 + num2 + num3) / 3
state = "합격" if res >= 80 else "탈락"
print("평균은 %d점이고, 결과는 %s입니다." % (res, state))
