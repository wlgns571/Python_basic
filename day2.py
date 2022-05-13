import random
# default 파라미터
def calc(i, j, factor=1):
    return i * j * factor

result = calc(10, 20)
print(result)
print(calc(10, 20, 30))

# named 파라미터
def report(name, age, score):
    print(name, score)
report(age=10, name="kim", score=80)

# 가변길이 파라미터
def fn_total(*number):
    tot = 0
    for n in  number:
        tot += n
    return tot
print(fn_total(2,3,10))
print(fn_total())

# 가변길이에 고정값 1
def fn_sum_mul(flag, *args):
    count = 0
    if flag == 'sum':
        result = 0
        for i in args:
            result += i
            count += 1
    elif flag == 'mul':
        result = 1
        for i in args:
            result *= i
            count += 1
    return  result, count
re, cnt = fn_sum_mul('mul', 2, 30)
print(cnt, '번', re )
