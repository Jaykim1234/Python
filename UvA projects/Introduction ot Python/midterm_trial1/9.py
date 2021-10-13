"""
Question 9
Imagine that you are looking at an 8-by-8 chessboard, where the squares are numbered from 1 to 8 both vertically and horizontally, starting from the bottom left corner.
A position on the board is represented by a tuple of integers, row number first. The position (3, 2), for example, represents the third row from the bottom and the second column from the left.
Write a function called main that accepts the initial position of a bishop chess piece and the target position of an intended move with the piece as two tuples.
The function should return the boolean value True if the move is valid, and False if it is not.
Note: A bishop can move any number of steps in any of the four diagonal directions.
Hint: Mark the valid moves on a piece of paper starting from some initial position. Compare the row and column coordinates of valid target positions with the coordinates of the initial position. If you notice any regularities, implement them as a check for the validity of a move. Also, perhaps take a look at the abs() function to shorten your code.
For example
If we are calling your function as:
main((4, 5), (7, 8))
then it should return the boolean:
True
"""



# def main(start,end):
    
#     spot = [i for i in start]
    
#     #Case 1 (+1, +1)

#     lst1 = []
#     row,col = spot[0],spot[1]
#     while (row not in [1,8]) and (col not in [1,8]) > 0:
#         row += 1
#         col += 1
#         new_spot = row,col
#         lst1.append(new_spot)
        
#     # Case 2 (-1,-1)

#     spot = [i for i in start]
#     lst2 = []
#     row,col = spot[0],spot[1]
#     while (row not in [1,8]) and (col not in [1,8]) > 0:
#         row -= 1
#         col -= 1
#         new_spot = row,col
#         lst2.append(new_spot)

#     # Case 3  (+1,-1)

#     spot = [i for i in start]

#     lst3 = []
#     row,col = spot[0],spot[1]
#     while (row not in [1,8]) and (col not in [1,8]) > 0:
#         row += 1
#         col -= 1
#         new_spot = row,col
#         lst3.append(new_spot)
#     print(lst3)   


#     # Case 4  (+1,-1)
#     spot = [i for i in start]

#     lst4 = []
#     row,col = spot[0],spot[1]
#     while (row not in [1,8]) and (col not in [1,8]) > 0:
#         row -= 1
#         col += 1
#         new_spot = row,col
#         lst4.append(new_spot)

#     lst_all = lst1+lst2+lst3+lst4
    
#     print('end',end)
#     print('lst_all',lst_all)

#     if end in lst_all:
#         return True
#     else:
#       return False


#Trial 2

def main(start,end):
    
    
    #Case 1 (+1, +1)
    lst1 = []
    row,col = start[0],start[1]
    while (row not in [1,8]) and (col not in [1,8]) :
        row += 1
        col += 1
        new_spot = row,col
        lst1.append(new_spot)

    # Case 2 (-1,-1)

    lst2 = []
    row,col = start[0],start[1]
    while (row not in [1,8]) and (col not in [1,8]):
        row -= 1
        col -= 1
        new_spot = row,col
        lst2.append(new_spot)

    # Case 3  (+1,-1)
    spot = [i for i in start]

    lst3 = []
    row,col = start[0],start[1]
    while (row not in [8]) and (col not in [1]):
        row += 1
        col -= 1
        new_spot = row,col
        lst3.append(new_spot)

    # Case 4  (-1,+1)


    lst4 = []
    row,col = start[0],start[1] ## Be careful at this point!!
    while (row not in [1]) and (col not in [8]):
        row -= 1
        col += 1
        new_spot = row,col
        lst4.append(new_spot)

    lst_all = lst1+lst2+lst3+lst4
    
    if end in lst_all:
        return True
    else:
        return False

print(main(*((1, 8), (4, 5))))
