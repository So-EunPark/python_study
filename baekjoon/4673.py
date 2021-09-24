def d(n):
    num=str(n)
    sum=0
    for i in list(num):
        sum += int(i)
    result = n+sum
    return result
sang=[]
# 생성자가 있는 숫자를 sang 리스트에 추가
for i in range(10001):
    sang.append(d(i))
# 1~10000까지 숫자중에서 sang 리스트에 있는 숫자 제외 = selfNumber
for i in range(1,10001):
    if i in sang:
        continue
    else:
        print(i)