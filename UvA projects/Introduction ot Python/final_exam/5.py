# lst = ['2', 'p', '9', '0', '0', 'v', '5', '3', '7', '1', '3', '6', '9', 'w', '4', 'Q', '5', '4', 'i', '6', '8', '1', 'x', '8', 'j']

# count = 0
# for i in lst:

#     if i in [str(num) for num in range(0,10)] :
#         count += 1
#     elif i == 'Q':
#         break
#     else: 
#         pass
# print(count)

def main(lst):
    count = 0
    for i in lst:

        if i in [str(num) for num in range(0,10)] :
            count += 1
        elif i == 'Q':
            break
        else: 
            pass
    return count