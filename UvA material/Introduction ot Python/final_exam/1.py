# lst = [59, 40, 43, 98, 94, 67, 15, 8, 16, 33, 18, 73, 99, 22, 0]

# dic = {}
# for index,val in enumerate(lst):
#     dic[index] = val - index
# print(dic)

def main(lst):
    dic = {}
    for index,val in enumerate(lst):
        dic[index] = val - index
    return dic

