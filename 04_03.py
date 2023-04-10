# # EX 01
# num_1 = int(input("정수를 입력하세요 : "))
# num_2 = int(input("약수를 입력하세요 : "))

# if num_1 % num_2 == 0:
#     print("약수입니다.")
# else:
#     print("약수가 아닙니다.")

# # EX 02

# temp = int(input("현재 온도를 입력하세요. : "))

# if temp >= 25:
#     print("반바지를 추천합니다.")
# else :
#     print("긴바지를 추천합니다.")

# # EX 03
# first_word = input("문자를 입력하세요. : ")
# word = ""
# if first_word == 'r' or first_word == 'R':
#     word = "Rectangle"
# elif first_word == 't' or first_word == 'T':
#     word = "Triangle"
# elif first_word == 'c' or first_word == 'C':
#     word = "Circle"
# else :
#     word = "Unknown"
# print(word)


# # EX 04

# a = int(input("원의 반지름 : "))

# if a <= 0:
#     print("잘못된 값입니다.")
# else:
#     print(round(a * a * 3.14, 2))

# # EX 05
# num = (input("3개의 정수를 입력하세요. (, 로 구분) : ")).split(",")

# row = 0

# num[0] = int(num[0])
# num[1] = int(num[1])
# num[2] = int(num[2])

# if num[0] <= num[1] and num[0] <= num[2]:
#     row = num[0]
# elif num[1] <= num[0] and num[1] <= num[2]:
#     row = num[1]
# else:
#     row = num[2]

# print(f'제일 작은 정수는 {row}입니다.')

# # EX 06

# import random

# user = int(input("기위(1), 바위(2), 보(3) : "))
# cpu = random.randint(1, 3)
# win = ""
# if (cpu == 1):
#     print("컴퓨터의 선택 : 가위")
#     if(user == 1):
#         win = "Tie"
#     if(user == 2):
#         win = "사용자"
#     if(user == 3):
#         win = "컴퓨터"
# elif (cpu == 2):
#     print("컴퓨터의 선택 : 바위")
#     if(user == 1):
#         win = "컴퓨터"
#     if(user == 2):
#         win = "Tie"
#     if(user == 3):
#         win = "사용자"
# else :
#     print("컴퓨터의 선택 : 보")
#     if(user == 1):
#         win = "사용자"
#     if(user == 2):
#         win = "컴퓨터"
#     if(user == 3):
#         win = "Tie"

# if win == "Tie":
#     print("비겼습니다.")
# else :
#     print(f"{win}가 이겼습니다.")


# # EX 07

# tall = int(input("키를 입력하세요 (cm) : "))
# age = int(input("나이를 입력하세요 : "))

# if (tall >= 140 and age >= 10):
#     print("타도 좋습니다.")
# else :
#     print("죄송합니다.")

# # EX 08

# data = (input("키와 체중을 입력하세요. (, 로 구분) : ").split(","))

# data[0] = int(data[0])
# data[1] = int(data[1])

# normal = (data[0] - 100) * 0.9

# if(normal == data[1]):
#     print("정상체중입니다.")
# elif(normal < data[1]):
#     print("과체중입니다.")
# else:
#     print("저체중입니다.")

# # EX 09
# import random

# type = random.randrange(4)

# num_1 = random.randrange(100) + 1
# num_2 = random.randrange(100) + 1

# if(type == 3):
#     while True:
#         num_1 = random.randrange(100) + 1
#         num_2 = random.randrange(100) + 1
#         if(num_1 % num_2 == 0):
#             break
    

# res = 0
# ans = ""
# type_str = ""

# if(type == 0):
#     res = num_1 + num_2
#     type_str = "+"
# elif(type == 1):
#     res = num_1 - num_2
#     type_str = "-"
# elif(type == 2):
#     res = num_1 * num_2
#     type_str = "*"
# else:
#     res = int(num_1 / num_2)
#     type_str = "/"

# ans = input((f'{num_1} {type_str} {num_2}의 값은 : '))

# if(str(res) == ans):
#     print("정답입니다.")
# else:
#     print(f"오답입니다. 정답은 : {res}")

# # EX 10

# x = float(input("X의 값을 입력하세요 (실수로 입력) : "))

# if(x <= 0):
#     print(f'f(x)의 값은 {x * x - (9*x) + 2}')
# else:
#     print(f'f(x)의 값은 {7 * x + 2}')

# # EX 11

# kg = int(input("무게(킬로그램) : "))
# m = float(input("키(미터) : "))
# bmi = kg / (m * m)
# print(f'당신의 BMI : {bmi}')

# if(bmi >= 30):
#     print("비만입니다.")
# elif(bmi >= 25):
#     print("과체중입니다.")
# else:
#     print("정상입나다.")

# # EX 12

# year = int(input("연도를 입력하세요. : "))
# ani = year % 12
# ani_str = ""

# if(ani == 0):
#     ani_str = "원숭이"
# elif(ani == 1):
#     ani_str = "닭"    
# elif(ani == 2):
#     ani_str = "개"
# elif(ani == 3):
#     ani_str = "돼지"
# elif(ani == 4):
#     ani_str = "쥐"
# elif(ani == 5):
#     ani_str = "소"
# elif(ani == 6):
#     ani_str = "호랑이"
# elif(ani == 7):
#     ani_str = "토끼"
# elif(ani == 8):
#     ani_str = "용"
# elif(ani == 9):
#     ani_str = "뱀"
# elif(ani == 10):
#     ani_str = "말"
# else:
#     ani_str = "양"

# print(f'{ani_str}입니다.')

# # EX 13

# year = int(input("연도를 입력하세요. : "))

# isYun = False

# if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
#     isYun = True
# if(isYun):
#     print("윤년입니다.")
# else:
#     print("윤년이 아닙니다.")

# # EX 14

# var_a = int(input("a를 입력하세요. : "))
# var_b = int(input("b를 입력하세요. : "))
# var_c = int(input("c를 입력하세요. : "))


# d = var_b ** 2 - 4 * var_a * var_c
# cnt_x = 0

# if(d > 0):
#     cnt_x = 2
#     x_0 = (-1 * var_b + ((var_b ** 2 + (-4 * var_a * var_c)) ** 0.5)) / (2 * var_a)
#     x_1 = (-1 * var_b - ((var_b ** 2 + (-4 * var_a * var_c)) ** 0.5)) / (2 * var_a)
#     print(f"실근은 {x_0}과 {x_1}입니다.")
# elif(d == 0):
#     cnt_x = 1
#     x_0 = (-1 * var_b + ((var_b ** 2 + (-4 * var_a * var_c)) ** 0.5)) / (2 * var_a)
#     print(f"실근은 {x_0}입니다.")
# else:
#     cnt_x = 0
#     print("실근이 존재하지 않습니다.")

# # EX 15

# int_input = int(input("정수를 입력하세요. : "))
# if(int_input % 3 == 0):
#     print("python", end=" ")
# if(int_input % 5 == 0):
#     print("Express")

# # EX 16

# ph = float(input("ph를 입력하세요. : "))
# type = ""
# isTrue = True
# if(ph == 7):
#     type = "중"
# elif(14 >= ph > 7):
#     type = "알칼리"
# elif(0 <= ph < 7):
#     type = "산"
# else:
#     print("수치 오류 입니다.")
#     isTrue = False

# if(isTrue):
#     print(f"{type}성 입니다.")