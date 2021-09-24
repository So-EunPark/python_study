t=int(input())
for _ in range(t):
    n, str = input().split()
    n=int(n)
    str=list(str)
    for i in range(len(str)):
        for _ in range(n):
            print(str[i],end='')
    print()