'''
1712번 손익분기점
21-08-10
--부등식계산하는 문제
'''

a,b,c = map(int,input().split())
if b >= c:
    print(-1)
else:
    print(int(a/(c-b))+1)