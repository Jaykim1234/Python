from itertools import combinations

def calculator(lst):
    even_lst = []
    odd_lst  = []

    if len(lst)== 1:
        return sum(lst)

    for idx in range(len(lst)):
        if (idx==0) or (idx%2 == 0):
            even_lst.append(lst[idx])
        else:
            odd_lst.append(lst[idx])
    value = (sum(even_lst) - sum(odd_lst))**2
    return value

def maxSubarrayValue(arr):
    emp_lst = []
    for lengths in range(1,len(arr)+1): 
        comb = list(combinations([num for num in range(len(arr))], lengths))
        # print(list(comb))
        for case in comb:
            emp_lst.append([arr[i] for i in list(case)])
    
    print('emp_lst', emp_lst)

    total_case = []
    
    case_lst = []
    for case_lst in emp_lst:
        total_case.append(calculator(case_lst))
        
    return max(total_case)
    # return emp_lst

maxSubarrayValue([-1,2,3,4,-5])

# def maxSubarrayValue(arr):
#     emp_lst = []
#     for lengths in range(1,len(arr)+1): 
#         comb = list(combinations(arr, lengths))
#         for case in comb:
#             emp_lst.append(list(case))
#     total_case = []
    
#     for case_lst in emp_lst:
#         total_case.append(calculator(case_lst))
#     print(emp_lst)
#     print(total_case)
#     # return total_case

# # maxSubarrayValue([1,-1,1,-1,1])
# maxSubarrayValue([-1,2,3,4,-5])


# for i in range(1,len(tmp)):
#     print(i)