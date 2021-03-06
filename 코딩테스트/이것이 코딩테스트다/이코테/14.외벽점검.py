# make a function that does permutation

n = 12
weak =[1, 5, 6, 10]
dist  = [1, 2, 3, 4]

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


# solution 1 need to check what the problem is
def solution(n, weak, dist):
    building_length = n
    all_case= list(all_perms(weak))

    initial_weak = [ i for i in weak]
    initial_dist = [j for j in dist]
    result=  float('inf')

    for case in all_case:
        # go only when friends are left or there are weak spots
        
        count = 0
        for spot in case:
            while (len(dist) >= 1) and (len(weak) >= 1):
        
                current_location = spot
                current_location = current_location  + dist.pop()
                count += 1 

                # Case 1
                if current_location >  building_length:
                    current_location -= building_length # start from 1

                    # Check whether friends has passed spots
                    lst1 = [j for j in weak if (spot <= j <= building_length) or (1 <= j <= current_location)]


                    # Remove weak spots when friends has passed
                    if len(lst1) !=0 :
                        for k in lst1:
                            weak.remove(k)

                    # when there is no weak spot
                    if len(weak) == 0:
                        break
                        
                # Case 2
                else:
                    # Check whether friends has passed spots
                    lst1 = [j for j in weak if spot  <= j <= current_location] 

                    # Remove weak spots when friends has passed
                    if len(lst1) !=0 :
                        for k in lst1:
                            weak.remove(k)

                    #Break when there is no weak spot
                    if len(weak) == 0 or len(dist)== 0:
                        break
    
            dist = initial_dist
            weak = initial_weak
            result = min(result, count)
            
    # return -1 when the result list has no values
 
    return result
n = 12
weak =[1, 5, 6, 10]
dist  = [1, 2, 3, 4]
solution(n, weak, dist)

# ?????? 
#?????? 2 need to check what the problem is


#  # make a function that does permutation

# def all_perms(elements):
#     if len(elements) <=1:
#         yield elements
#     else:
#         for perm in all_perms(elements[1:]):
#             for i in range(len(elements)):
#                 # nb elements[0:1] works in both string and list contexts
#                 yield perm[:i] + elements[0:1] + perm[i:]



# def solution(n, weak, dist):
#     initial_dist = dist
#     building_length = n
#     all_case= list(all_perms(weak))
#     result_box = []

#     for case in all_case:
        
#         count = 0
#         for spot in case:
#             # reset the dist list when each case is over
#             dist = initial_dist
            
#             # go only when friends are left or there are weak spots
#             print('dafadsf',len(dist))
#             while (len(dist) != 1) or (len(weak) != 1):
#                 print('max',max(dist))

#                 current_location = spot
#                 current_location = current_location  + max(dist)
#                 dist.remove(max(dist))
#                 count += 1 


#                 # Case 1
#                 if current_location >  building_length:
#                     current_location -= building_length # start from 1

#                     # Check whether friends has passed spots
#                     lst1 = [j for j in weak if (spot <= j <= building_length) or (1 <= j <= current_location)]


#                     # Remove weak spots when friends has passed
#                     if len(lst1) !=0 :
#                         for k in lst1:
#                             weak.remove(k)

#                     # when there is no weak spot
#                     if len(weak) == 0:
#                         result.append(friends_num)


#                 # Case 2
#                 else:
#                     # Check whether friends has passed spots
#                     lst1 = [j for j in weak if spot  <= j <= current_location] 

#                     # Remove weak spots when friends has passed
#                     if len(lst1) !=0 :
#                         for k in lst1:
#                             weak.remove(k)

#                     #Break when there is no weak spot
#                     if len(weak) == 0:
#                         result.append(count)

#     # return -1 when the result list has no values
#     if len(result) == 0:
#         return -1
#     else:
#         return min(result)
    
       