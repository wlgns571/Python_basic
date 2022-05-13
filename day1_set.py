# set 중복이 없는
myset = {1, 3, 4, 5, 1} # 중괄호
print(myset)
test = {}
print(type(test))
myset2 = set()
print(type(myset2))
myset2.add(10)
print(myset2)

# 여러개 추가
myset2.update({4, 99, 10})
print(myset2)

# 하나만 삭제
myset2.remove(10)
print(myset2)

# 모두 삭제
myset2.clear()
print(myset2)

# 입력 받은 수 만큼
# 로또 번호 생성해 주세요
import random
num = int(input("몇개 만드시겠습니까?: "))
ranList = set()
for i in range(num):
    for j in range(6):
        ran = random.randint(1,43)
        ranList.add(ran)
    print(ranList)
    ranList.clear()


