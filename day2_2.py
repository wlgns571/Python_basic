import os
# root = os.getcwd()
root = '/'
searchNm = input('찾고 싶은 파일명: ')
# 해당 위치의 파일 정보 가져오기
files = os.listdir(root)
for file in files:
    # print(file)
    # 경로 + 파일 명
    path = os.path.join(root, file)
    # print(path)
    if searchNm in file:
        check = input('이걸 찾는가? ' + path + '?(y/n)')
        if check == 'y':
            break