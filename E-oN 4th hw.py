a = input("숫자를 입력하세요 (쉼표로 구분) :")
a = a.split(",") 
a = list(map(int, a))

b = len(a)
for i in range(0,b-1):
  for j in range(i+1, b):
    if a[i] > a[j] :
      x = a[i] 
      a[i] = a[j]
      a[j] = x
print(a)

#bubble sort
