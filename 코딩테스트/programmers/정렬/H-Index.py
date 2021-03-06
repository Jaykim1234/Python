"""
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
입출력 예
citations	return
[3, 0, 6, 1, 5]	3 
0 1 3 5 6

5-2

위에가 3개 이상 있어야 되고 밑에꺼는 3이하이여야 한다.
입출력 예 설명
이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

※ 공지 - 2019년 2월 28일 테스트 케이스가 추가되었습니다.
"""

def solution(lst):
    lst = sorted(lst)
    length = len(lst)
    middle_spot = length//2 
    middle_spot_num = lst[length//2] 

    if middle_spot_num >= length - middle_spot  


    

def solution(lst):
    lst = sorted(lst)
    length = len(lst)
    middle_spot = length//2 
    middle_spot_num = lst[length//2] 
    middle_spot_num_next = lst[length//2+1]
    
    if (middle_spot_num_next >  length - middle_spot) and (middle_spot_num <= length - middle_spot):
        return middle_spot_num 
    
    if length > 100:
        if middle_spot_num >= length - middle_spot:
            return solution(lst[:middle_spot])
        elif middle_spot_num <= length - middle_spot: # 가운데 있는 수 보다 큰 숫자들의 개수가 가운데 있는 수 보다 크거나 같을 때
            return solution(lst[middle_spot::])
    else:
        if middle_spot_num >= length - middle_spot:
            while  (middle_spot_num_next >  length - middle_spot) and (middle_spot_num <= length - middle_spot) :
                pass
        elif middle_spot_num <= length - middle_spot: # 가운데 있는 수 보다 큰 숫자들의 개수가 가운데 있는 수 보다 크거나 같을 때
            return solution(lst[middle_spot::])

solution([3, 0, 6, 1, 5])

def solution0(lst):
    lst = sorted(lst)
    for idx_1 in range(length):
        up_equal_count = 0
        down_count = 0

        while True:
            for idx_2 in range(length):
                if lst[idx_1] >= lst[idx_2]:
                    up_equal_count += 1
                else:
                    down_count += 1
            return lst[idx_1]



solution([3, 0, 6, 1, 5])

# print(sorted([1,5,2,8,3]))



# n편 중, h번 이상 인용된 논문이 h편 '이상'이고 나머지 논문이 h번 이하 인용