


# # stage 1

# stages.count(1)/(len(stages)- len[i for i in stages if i > 1])

# # stage 2

# stages.count(2)/(len(stages) - len[i for i in stages if i > 2])

# # # stage 3

# # stages.count(3)/(len(stages) - len[i for i in stages if i > 3])

# # # stage N

# # stages.count(N)/(len(stages) - len[i for i in stages if i > N])


# # 함수화 런타임 에러

# def solution(N, stages):
#     stage_sorted = [num for num in range(1,N+1)]
#     result = []

#     for each_stage in stage_sorted:
    
#         num_of_fail   = stages.count(each_stage)
#         total_people_each_stage  = len([i for i in stages if i >= each_stage])
#         failure_rate  = num_of_fail / total_people_each_stage

#         result.append([each_stage, failure_rate])

#     ordered_result = sorted(result, key= lambda x : x[1], reverse= True)

#     answer = [stage for stage, rate in ordered_result]
    
#     return answer

# solution(5, [2, 1, 2, 6, 2, 4, 3, 3])


# # 두 번째 방법 : find 함수를 이용해서 전체 참여자 수를 찾는다

# lst = [2, 1, 2, 6, 2, 4, 3, 3]
# lst.sort()
# lst

# lst_str = [str(i) for i in lst]

# str_number = ''.join(lst_str)
# str_number 
# str_number.find(str(3))


def solution3(N, stages):
    stage_sorted = [num for num in range(1,N+1)]
    #1, 2, 3, 4, 5

    stages_str = [str(i) for i in stages]
    stages.sort()
    # 모든 요소 다 스트링으로 변환

    str_number = ''.join(stages_str)
    #스트링으로 변환 한거 한줄로 다 붙힌다.

    result = []

    for each_stage in stage_sorted:
    
        num_of_fail   = stages.count(each_stage)
        total_people_each_stage  = len(stages) - str_number.find(str(each_stage))
        failure_rate  = num_of_fail / total_people_each_stage

        result.append([each_stage, failure_rate])

    ordered_result = sorted(result, key= lambda x : x[1], reverse= True)

    answer = [stage for stage, rate in ordered_result]
    
    return answer

solution3(5, [2, 1, 2, 6, 2, 4, 3, 3])