# n = 5
# m = [2,3,1,2,2]
# m.sort() # 1 2 2 2 3

# result = 0
# count  = 0

# for i in m:
#     count += 1
#     if count >= i:
#         result += 1
#         count   = 0


# 외우고 푼거
n = 5
m = [2,3,1,2,2]
m.sort()

result = 0
count = 0

for i in m:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)