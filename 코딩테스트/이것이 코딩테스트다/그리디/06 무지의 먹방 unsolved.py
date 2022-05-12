import heapq

def solution(food_times, k):
    if sum(food_times) <= k: 
        return -1
    
    q = []
    for i in range(len(food_times)):         
        # heapq.heappush(heap, item)
        # 힙 불변성을 유지하면서, item 값을 heap으로 푸시합니다.       
        heapq.heappush(q, (food_times[i], i +1))       

    sum_value = 0
    previous  = 0

    length = len(food_times)

    while sum_value + (q[0][0]- previous)*length <= k: #  가장 작은 수랑 - previous  이거 곱하고 
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]
    
food_times = [3,1,2]
k = 5
result = 1

solution(food_times, k)