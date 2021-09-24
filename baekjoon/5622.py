dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
str=input()
answer=0
for l in range(len(str)):
    for i in dial:
        if str[l] in i:
            answer += dial.index(i)+3
print(answer)

'''
21-08-09
이번 문제는 구글링 찬스를 좀 썼다...^^
어떻게 문제를 풀까 생각하면서 다양한 방법을 떠올렸는데, 나한테는 최대한 간단하게 문제를 해결하는 능력을 좀 키워야 되겠다고 생각이 들었다.

1. 집합 연산자 사용?
2. Ascii code 사용?
3. Dictionary 사용?
이런 생각이 들면서.. 자료구조랑 Collection 공부를 정말 해야겠다는 생각이 들었닼ㅋㅋㅋ ㅠㅜ
모든 문제를 항상 복잡하게 생각하고 복잡하게 풀려고 하는 영향이 있는데,, 다른 사람들 답을 보면 항상 엄청 간단하고 심플하지만 강력하게 해결하신다.
화이팅팅팅!
'''