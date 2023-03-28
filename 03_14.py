"""
a = int(input("물건의 가격"))
b = int(input("지불한 돈"))

res = a - b;
# 407 
_100 = int(res / 100)

res %= 100

_10 = int(res / 10)

res %= 10

_1 = res

output = f'100원 {_100}개 10원 {_10}개 1원 {_1}개'

print(output)
"""

a = input("키 몸무게 입력 (, 로 구분, 키는 m 단위로 입력)").split(",")

res = round(int(a[1]) / float(a[0])**2, 2)

print(res)



