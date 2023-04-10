_name = input("이름 입력 : ")
cur_year = int(input("현재년도 입력 : "))
bd_year = int(input("출생년도 입력 : "))
print("{0}님의 한국 나이는 {1}살입니다." .format(_name, cur_year - bd_year + 1))