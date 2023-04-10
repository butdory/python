num = input("num: ")
n = len(num)

res = ''
for i in range(n):
    if i > 0 and (n-i) % 3 == 0:
        res += ','
    res += num[i]

print(res)
