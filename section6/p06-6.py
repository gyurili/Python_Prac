d = 2
n = 1

while n <= 9:
    while d <= 9:
        print("%dX%d=%d" % (d, n, d * n), end="\t")
        d += 1
    print()
    n += 1
    d = 2
