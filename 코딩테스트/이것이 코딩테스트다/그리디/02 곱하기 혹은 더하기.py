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

for i in input:
    print(int(i))


# num = input[0]
# int_num = int(num)

# for i in input:
#     if int_num <= 1 or int(i) <= 1:
#         int_num += i
#     else:
#         int_num*= i
# print(int_num)