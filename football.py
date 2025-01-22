i = list(input())
l = len(i)
stat = "NO"
for j in range(l - 6):
    if len(set(i[j : j + 7])) == 1:
        stat = "YES"
        break
print(stat)
