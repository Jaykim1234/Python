# input = '567'

# # 이거는 1+1 >1*1임을 생각을 안함
# result = 1
# for i in input:
#     if int(i) != 0:
#         result = result * int(i) 
# print(result)

# 답지
# data = input()

# result =  int(data[0])

# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result += num
        
# 답지 보고 다시 푼 것
input = '567'

for i in range(1, len(input)): # 'for i in input 하면' 왜 오류가 뜨는지 모르겠다. 
    num = int(input[i])
    if num <= 1 or int(i) <= 1:
        num += i
    else:
        num*= i
print(num)