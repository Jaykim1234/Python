# lst  = [(3, 3), (3, 1), (6, 3), (2, 8), (5, 5)]
# lst2 = []
# for tup in lst:
#     if  tup[0] >= tup[1]:
#         lst2.append(tup[0]+ tup[1])
#     else:
#         lst2.append(None)
# print(lst2)

def main(lst):
    
    lst2 = []
    for tup in lst:
        if  tup[0] >= tup[1]:
            lst2.append(tup[0]+ tup[1])
        else:
            lst2.append(None)
    return lst2