def solution(priorities, location):
    
    answer_lst = []

    while priorities[0] < max(priorities):
        if location > 0:
            location -= 1
            priorities.append(priorities.pop(0))
        else:
            location = len(priorities) -1
            priorities.append(priorities.pop(0))
    
    answer_lst.append(priorities[0])

    return location+1