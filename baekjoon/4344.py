c=int(input())

for i in range(c):
    x=map(int,input().split())
    b=list(x)
    cnt=0
    avg=(sum(b)-b[0])/b[0]
    for j in range(1,len(b)):
        if b[j]>avg:
            cnt+=1
    result=(cnt/b[0])*100
    print("{:.3f}%".format(result))
# 커밋