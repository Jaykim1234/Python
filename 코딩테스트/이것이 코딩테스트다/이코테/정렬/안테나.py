# N = 4
# locations = [5,1,7,9]

## 시간초과
# N = int(input())
# locations = list(map(int, input().split()))

# N = 4
# locations = [5,1,7,9]

# answer = 10**10

# for index,spot in enumerate(locations):
#     distance = sum([abs(location-spot) for location in locations ])
#     answer = min(distance,answer)

# print(answer)

# 시도 2 평균에 가장 가까운 값 구하기

# N = 4
# locations = [5,1,7,9]

N = int(input())
locations = list(map(int, input().split()))

mean_loc = sum(locations)/len(locations)

answer_index = 0

distance = [abs(location-mean_loc) for location in locations]
print(distance)
print(locations[distance.index(min(distance))])


# n = int(input())
# houses = list(map(int, input().split()))
# houses.sort()
# print(houses[len(houses)//2-1])





