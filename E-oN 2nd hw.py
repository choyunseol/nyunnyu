#홀수 짝수 구별하는 프로그램

x = (input('원하는 자연수를 입력하세요 :')) #임의의 수 입력

while (x.isdigit() != 1 or int(x) == 0) : #입력받은 수가 자연수가 아닐 경우
    x = (input('다시 입력하세요. :'))

y = int(x) #문자열을 숫자로 전환

if (y % 2 == 0): #홀,짝 판단
    print ("입력하신 수는 짝수입니다.")
else :
    print ("입력하신 수는 홀수입니다.")
