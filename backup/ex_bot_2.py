import os
import datetime
# 입력 받은 메세지를 diary.txt 파일에 적어 놓도록
# (1) 받은 메세지에서 /diary 제거
# (2) diary 폴더가 없으면 생성
# (3) 해당 '일자.txt' 파일에 내용을 기입

now = datetime.datetime.now()
formattedDate = now.strftime("%Y%m%d_diary.txt")
f = open(formattedDate,'a')