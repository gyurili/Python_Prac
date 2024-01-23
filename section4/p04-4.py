num = int(input("라면의 개수를 입력하세요: "))
res = num // 20 if (num % 20) == 0 else num // 20 + 1
print("%d개의 라면을 담으려면 %d박스가 필요합니다." % (num, res))
