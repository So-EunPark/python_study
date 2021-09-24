str=list(input())
answer=[-1 for i in range(26)]
for i in range(len(str)):
    index = ord(str[i])-97
    if answer[index] == -1:
        answer[index]=i
for i in range(len(answer)):
    print('{0}'.format(answer[i]), end=' ')