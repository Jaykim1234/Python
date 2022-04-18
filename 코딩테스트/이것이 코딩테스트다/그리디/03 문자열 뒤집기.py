s = '0001100'
print(set(s))


def solution(s):
    answer = 100000
    for i in set(s):
        answer = min(answer, len([ind for ind in s.split(i) if ind != '']))
    print(answer)
    
# solution(s)

# Answer

data = '0001100'

count0 = 0 # 전부 0으로 바꿈
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        if data[i] == 0:
            count0 += 1
        else:
            count1 += 1
            
answer = min(count0, count1)
print(answer)