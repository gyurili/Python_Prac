second = int(input("초를 입력하세요: "))
h = second / 3600
m = (second % 3600) / 60
s = m % 60
print("변환 결과는 %d시간 %d분 %d초입니다." % (h, m, s))
