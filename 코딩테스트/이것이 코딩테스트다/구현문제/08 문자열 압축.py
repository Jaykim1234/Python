s1 = 'aabbaccc'
s2 = 'abcabcabcabcdededededede'
s3 = 'xababcdcdababcdcd'

def solution2(s):
    answer = len(s)

    for step in range(1, len(s)//2 + 1):
        prev  = s[0: step]
        count = 1
        compressed = ""
        for j in range(step, len(s), step):
            if prev == s[j: step+j]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j: step+j]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer =  min(answer, len(compressed))   
    return answer

print(solution2(s2))

def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 +1): # step을 1부터 반까지
        compressed = ""
        prev = s[0:step] # 처음 단위로 지정
        count = 1
        for j in range(step, len(s), step): # 단위 step 만큼 증가시킴
            if prev == s[j:j+step]:  # j는 step 뒤에 한 단위
                count += 1 # 센 것 늘림
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j: j +step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer

solution(s1)

# def solution(s):
#     for i in range(1, len(s)//2):
#         cnt = 1
#         a = s[0:i]
#         for j in range(0, len(s)//2):
#             if a == s[0+j:i+j]:
            
#     return s

# solution(s1)