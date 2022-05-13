# # 텍스트 생성
# f = open('delay.txt', 'a')
# f.write('오늘 지각자 !!! \n')
# while True:
#     n = input('오늘 지각한 사람?(종료:q) ')
#     if "q" == n:
#         break
#     f.write(n)
#     f.writelines('\n')
# f.close()

# 폴더 생성 및 이동
import shutil
import os
from_ = 'test.py'
to_ = './backup'
if not os.path.exists(to_):
    # 폴더 생성
    os.makedirs(to_)
# 파일 이동
shutil.move(from_, to_)

# 파일 지우기
# import os
# print(os.getcwd()) # 현재위치
# # fileNm = 'delay.txt'
# fileNm = 'test'
# if os.path.exists(fileNm):
#     # 파일이면
#     if os.path.isfile(fileNm):
#         os.remove(fileNm) # 파일 삭제
#     if os.path.isdir(fileNm):
#         os.rmdir(fileNm)
#     print('삭제 되었습니다.')

