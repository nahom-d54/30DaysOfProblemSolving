i = int(input())
j = list(map(int, input().split(" ")))
j.sort(reverse=True)
s = sum(j) / 2
m = 0
c = 0
for k in j:
    m += k
    c += 1
    if m > s:
        break
print(c)
