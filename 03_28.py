
# a = input("키 몸무게 입력 (, 로 구분)").split(",")

# res = round(int(a[1]) / (float(a[0])/100) ** 2, 2)

# print(res)

# _input = int(input("키를 입력하세요. (cm) : "))
# print(f'표준 체중은 {(_input - 100) * 0.9}입니다.')

num = input("num : ")
i = 1
res = ""
while True:
    if(i >= len(num)):
        res = num
        break
    if(int(len(num[i : len(num)])) % 3 == 0):
        res = num[0 : i] + "," + num[i : len(num)]
        num = res
        i += 1
    i += 1
print(res)
# 1, 2, 3 남은 숫자의 자리수가 3의 배수일 때 , 추가 