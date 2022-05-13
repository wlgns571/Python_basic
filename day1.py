from builtins import print

print('hi')
a = '안녕하세요'
print(a)
# 문자열 곱하기
print(a*10)
a = '''hi
hello
안녕
'''
print(a)
# 문자열 나누기
b = 'Life is too short'
c = b.split() # 매개변수 없으면 공백으로 자름
print(c)
d = "a:b:c:d"
f = d.split(':')
print(f)
# 입력 받기
# a = input('문자를 입력하세요: ')
# print(a)
# num = int(input('숫자를 입력 하세요: '))
# print(num)
# if num < 10:
#     print('10보다 작음')
# elif num == 100:
#     print('100 이다!')
# else:
#     print('100 보다 큼')
# 동적배열 List
a = []
b = [1, 2, 3]
c = [1, 2, 'list', 'is']
d = [1, 2, [3, 4]]
# 리스트 인덱스 -1 : 마지막 요소 -2  : 뒤에서 두번 째
# 중첩 리스트 d[2][0] <- d의 3번째 요소의 0번째 요소
print(c[-1])
print(d[2][0])
# 슬라이스
# [처음인덱스 : 마지막인덱스 +1]
print(d[1:3])
f = ['This', 'is', 'a', 'book', 'is']
print(f.count('is'))
# 리스트 곱
print(d * 100)
# for문 style 1
arr = ['one', 'two', 'three']
for i in arr:
    print(i)
# for문 style 2 : index, value 둘다 필요할때
for i, v in enumerate(arr):
    print(i, '번째:', v)
# for문 style 3 : 단순 반복
for i in range(1, 5):
    print(i, end = ' ') # 모아서 프린트 하고 싶을때
# 입력 받는 수 만큼 hi를 출력하시오
# num = int(input('숫자를 입력해주세요: '))
# str = '''hi
# '''
# print(str * num)
# for i in range(num):
#     print('hi')
import random
# 1 ~ 10 사이 정수값 반환
num = random.randint(1, 10)
print(num)
while True:
    user_num = int(input('1 ~ 10 임의의 수를 맞춰 보시오: '))
    if num == user_num:
        print('정답입니다.')
        break
    else:
        print('다릅니다.')
        if num > user_num:
            print('UP')
        elif num < user_num:
            print('DOWN')


