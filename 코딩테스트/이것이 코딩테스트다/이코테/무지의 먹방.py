"""
무지의 먹방 라이브

평소 식욕이 왕성한 무지는 자신의 재능을 뽐내고 싶어 졌고 고민 끝에 카카오 TV 라이브로 방송을 하기로 마음먹었다.

그냥 먹방을 하면 다른 방송과 차별성이 없기 때문에 무지는 아래와 같이 독특한 방식을 생각해냈다.

회전판에 먹어야 할 N 개의 음식이 있다.
각 음식에는 1부터 N 까지 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요된다.
무지는 다음과 같은 방법으로 음식을 섭취한다.

무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.
마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.
무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다.
다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말한다.
회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정한다.
무지가 먹방을 시작한 지 K 초 후에 네트워크 장애로 인해 방송이 잠시 중단되었다.
무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 한다.
각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times, 네트워크 장애가 발생한 시간 K 초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하라.

제한사항
food_times 는 각 음식을 모두 먹는데 필요한 시간이 음식의 번호 순서대로 들어있는 배열이다.
k 는 방송이 중단된 시간을 나타낸다.
만약 더 섭취해야 할 음식이 없다면 -1을 반환하면 된다.
"""


# #trial 1 런타임 에러

# def solution(ft,k):
    
#     index = 0

#     while k > 0 and set(ft) != {0}:
#         k -=1
    
#         if ft[index] != 0:
#             ft[index] -= 1
    
#         else:
#             #ft 가 0 이면 다음껄로 넘겨서 ft[index]을 -1을 한다.
#             index += 1
#             ft[index] -= 1

    
#         # 음식을 마지막 것을 섭취하면 처음 걸로 돌아갈 수 있도록 코딩
#         if index == len(ft) -1:
#             index = 0
#         else:
#             index += 1
#     #다음에 먹을 음식의 index를 현재 index로 지정
#     answer_next_index = index  

#     # 마지막으로 먹은 음식의 인덱스가 제일 마지막에 있는 경우
#     # 다음 먹을 음식의 인덱스는 첫번째 부터 시작
#     if index == len(ft) -1:
#         index = 0
#         # 다음 먹을 음식이 남아있지 않다면 & index가 주어진 범위 안일 때
#         while ft[index] == 0 and index <= len(ft) -1 : 
#             index += 1       # 그 다음 index로 넘어간다.
        
#         answer_next_index = 0
#     else:
#         answer_next_index += 1
    
#     if set(ft) != {0}:
#         return -1
#     else:    
#         return answer_next_index

# solution([3,1,2],5)
    
# from queue import PriorityQueue

# q = PriorityQueue()

# for i in range(10):
#     q.put(i)
# print(q)
# print(q.get()[0])
# q
# print(q.get()[0])

# trial 2 

from queue import PriorityQueue

def solution(ft,k):
    
    if sum(ft) > k:
        return -1
    
    q = PriorityQueue()

    for i in range(len(ft)):
        q.put(ft[i],i+1)


    
        # 음식을 마지막 것을 섭취하면 처음 걸로 돌아갈 수 있도록 코딩
        if index == len(ft) -1:
            index = 0
        else:
            index += 1
    #다음에 먹을 음식의 index를 현재 index로 지정
    answer_next_index = index  

    # 마지막으로 먹은 음식의 인덱스가 제일 마지막에 있는 경우
    # 다음 먹을 음식의 인덱스는 첫번째 부터 시작
    if index == len(ft) -1:
        index = 0
        # 다음 먹을 음식이 남아있지 않다면 & index가 주어진 범위 안일 때
        while ft[index] == 0 and index <= len(ft) -1 : 
            index += 1       # 그 다음 index로 넘어간다.
        
        answer_next_index = 0
    else:
        answer_next_index += 1
    
    if set(ft) != {0}:
        return -1
    else:    
        return answer_next_index

solution([3,1,2],5)
    