num = int(input("4자리 사원번호를 입력하세요: "))
res = "오전" if (num % 10) >= 5 else "오후"
print("근무시간은 %s입니다." % res)
