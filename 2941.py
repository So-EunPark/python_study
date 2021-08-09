'''
2941번 크로아티아 알파벳

해결방법
1. 입력받은 문자열의 각 알파벳이 크로아티아 알파벳 첫글자라면 대조해서 체크하기.
str = 'ddz=z='
head = ['c','d','l','n','s','z']

answer = 0
cro=[]

for i in range(len(str)):
    if str[i] in head:
        cro.append(str[i])
        w=''.join(cro)
        if
        continue
    else:
        answer += 1
        continue
print(answer, )

음...

또 구글링의 도움을 받게 되었다.
python의 내장 라이브러리는 너무 강력한 것 같다.
replace() 라는 문자열 조작 메소드가 있는데! 이걸 이용하면 단 2줄만에 문제를 해결 할 수 있다. 완전 어이가 업슴 ㅜㅜ
다음에는 구글링 하지 말고 최대한 스스로 문제를 해결하려고 해보자!!
'''

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()

for i in cro:
    str = str.replace(i, '*')
print(len(str))
