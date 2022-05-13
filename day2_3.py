import os
# 재귀함수 호출
# def fn_print_files(root):
#     files = os.listdir(root)
#     for file in files:
#         path = os.path.join(root, file)
#         print(path)
#         if os.path.isdir(path):
#             fn_print_files(path)
#
# fn_print_files('/home/pc54/Downloads')
#
# def fn_print_files2(root, param):
#     files = os.listdir(root)
#     for file in files:
#         path = os.path.join(root, file)
#         if param in file:
#             msg = input(path + ' 이거?(y/n)')
#         # print(path)
#         if os.path.isdir(path):
#             fn_print_files2(path, param)
#
# fn_print_files2('/home/pc54/Downloads', '김지훈')

path = '/home/pc54/Downloads'
# 디폴트 top-down : 상위 -> 하위로
# topdown = False : 하위에서 -> 상위로
# for root, dirs, files in os.walk(path):
for root, dirs, files in os.walk(path, topdown=False):
    print(root, dirs, files)