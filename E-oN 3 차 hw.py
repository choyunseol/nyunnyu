a = input("숫자를 입력해주세요.")
a = a.split(",")

def add(a):
    sum = 0
    for i in a:
        sum += int(i)
    return sum

print(add(a))
