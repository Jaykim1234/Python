"""

평범한 배낭
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	57308	21103	13716	35.368%
문제
이 문제는 아주 평범한 배낭에 관한 문제이다.

한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

입력
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

입력으로 주어지는 모든 수는 정수이다.

출력
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

예제 입력 1 

4 7
6 13
4 8
3 6
5 12


예제 출력 1 
14

"""
# from sys import stdin
# n, w = map(int, input().split())
# weights, value = [] , []

# for _ in n:
#     a, b = map(int, input().split())
#     weights.append(a)
#     value.append(b)

from itertools import combinations

n, w  = 4, 7
wv = [[6,13], [4,8], [3,6], [5,12]]

print(list(combinations(wv, 3)))

emp_lst = []
for i in range(1, wv):
    comb = combinations(wv, i)
    print(comb)

print(emp_lst)


# print(list(map(lambda x: list(x) ,list(combinations(wv, 3)))))
# wv.sort(key=lambda x: (x[1], x[0]), reverse = True)

# print(wv)

# lst = map(sorted(), wv)
# value   = [7, 13, 8, 6, 12]
# weights = [4, 6,  4, 3, 5]
# logs.sort(key=lambda x: (x.split('_')[0], -int(x.split('_')[1])))


