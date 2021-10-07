"""
단어 변환
문제 설명
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

제한사항
각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.
입출력 예
begin	target	words	return
"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0
입출력 예 설명
예제 #1
문제에 나온 예와 같습니다.

예제 #2
target인 "cog"는 words 안에 없기 때문에 변환할 수 없습니다."""

print(len(set('hot') -set('ho')))


def checker(lst1, lst2):
    check = 0
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            check += 1
    if check == len(lst1) -1:
        return True
    else:
        return False

    
import copy
def bfs(begin, target, words):
    words_count = len(words)
    lst = [False for i in range(len(words))]
    answer = words_count
    queue  = []
    round_c = 0
    queue.append([lst, round_c, begin])
    Find = False
    while queue:    
        
        if round_c == words_count and current_word != target:
            queue.pop(0)

        else:
            cur_lst, round_c, current_word = queue.pop(0)

            for idx in range(words_count):
                if cur_lst[idx] == False:
                    if checker(current_word, words[idx]) ==  True:    
                        new_lst = copy.deepcopy(cur_lst)
                        new_lst[idx] = True 

                        if words[idx] == target:
                            answer = min(answer, round_c + 1)
                            Find = True
                        else:
                            queue.append([new_lst, round_c + 1, words[idx]])
            round_c += 1
    return answer if Find == True else 0

print(bfs("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))


