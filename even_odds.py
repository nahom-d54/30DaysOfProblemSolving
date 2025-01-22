n, k = list(map(int, input().split(" ")))

odds = -(n // -2)
if k <= odds:
    n = 2 * k - 1
else:
    n = 2 * (k - odds)
print(n)
