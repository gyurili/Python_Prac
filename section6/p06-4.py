s = set()

while len(s) < 5:
    num = int(input("0~9사이의 정수를 입력하세요 >>>"))
    s.add(num)

print("모두 입력되었습니다")
print("입력된 값은", s, "입니다")
