num = input("차량번호를 입력하세요: ")

res = int(num[-1])
if res % 2 == 0:
    print("차량번호 %s는 오늘 운행 가능합니다." % num)
else:
    print("차량번호 %s는 오늘 운행 불가능합니다." % num)
