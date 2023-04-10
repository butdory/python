"""
_input = int(input("반지름 입력 : "))
pi = 3.14

area = _input * _input * pi

print("원의 넓이는 : ", area)
"""

"""
import turtle as t


t.shape("turtle")


for i in range(3):
    t.circle(100)
    t.penup()
    t.forward(100)
    t.pendown()
    
t.done()

"""



int_input = int(input("정수를 입력하세요. : "))
if(int_input % 3 == 0):
    print("python", end=" ")
if(int_input % 5 == 0):
    print("Express")