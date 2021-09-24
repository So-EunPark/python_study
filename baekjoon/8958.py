# str="OOOOXOOOOXOOOOX"
result=[]

n=int(input())
for j in range(n):
    str=input()
    for i in range(len(str)):
        if i==0:
            if str[0]=="O":
                result.append(1)
                continue
            else:
                result.append(0)
                continue
        if str[i]=="O":
            if result[i-1]!=0:
                result.append(result[i-1]+1)
            else:
                result.append(1)
        else:
            result.append(0)
    print(sum(result))
    result=[]