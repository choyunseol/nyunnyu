n = int(input("숫자를 입력하세요 :")) #피자조각의 개수를 입력받음
a = n // 2 #조각을 2로 나눴을 때의 몫
b = n % 2
if b==1 :
  a+=1    #홀수일 경우 몫에 1을 더함

k = 0
j = 0
for i in range (n, a-1, -1) : # i를 n부터 a까지 1씩 감소시키는 반복문
  e = 1
  h = 1
  for y in range (i-j+1, i+1) : # y를 i-j+1부터 i까지 1씩 증가시키는 반복문 (조합의 분자)
    e = e*y
  for z in range (1,j+1) : # z를 1부터 j까지 1씩 증가시키는 반복문 (조합의 분모)
    h = h*z
  k = k + int(e/h) #구한조합들을 누적으로 더함
  j+=1  # j값 1 증가

print(k)
