# 0이상 1000이하의 수를 한줄에 하나씩 10개 입력받은뒤, 각 수를 42로 나눈 나머지 중 서로 다른 나머지의 개수를 알아내는 프로그램

a = []
b = []
for i in range(10):
    c = int(input("숫자를 입력하세요"))
    while not ((0 < c or c == 0) and (c < 1000 or c ==1000)):
        c = int(input("제대로 된 숫자를 입력하세요"))

    a.append(c)

for i in a:
    b.append(i % 42)
print("입력된 리스트는" , a , "입니다")
print(f"서로 다른 나머지는 {len(set(b))} 개이다.")
