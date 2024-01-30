n = 1

while n <= 100:
    if n % 10 == 0:
        print("%d" % n, end="\n")
    else:
        print("%d" % n, end="\t")
    n += 1
