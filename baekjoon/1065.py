def hansu(num):
    n = list(str(num))
    a = []
    for i in range(len(n)):
        a.append(int(n[i]))
    b = []
    for i in range(len(a)):
        if i == len(a) - 1:
            break
        b.append(a[i + 1] - a[i])
    if b[0] == b[1]:
        return True
    else:
        return False


x = int(input())
if 0 < x < 100:
    print(x)
elif 100 <= x:
    answer = 99
    for j in range(100, x + 1):
        if hansu(j):
            answer += 1
    print(answer)