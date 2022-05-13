# dict key:value
score = {'철수':90, '민수':85, '영희':100}
# dict는 단순 for문 일때 key 를 반환
for key in score:
    print(key)
    print(score[key])
# 수정
score['철수'] = 10
# 추가
score['팽수'] = 99
print(score)