col = 1
row = 1
for i in range(5):
    l = input().split(" ")
    if "1" in l:
        col = l.index("1") + 1
        break
    row += 1
m = abs(row - 3) + abs(col - 3)
print(m)
