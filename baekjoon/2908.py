li = list(input().split())
for i in range(len(li)):
    li[i] = int(li[i][::-1])
print(max(li))