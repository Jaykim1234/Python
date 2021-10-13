"""
Hugo explained in one of his videos for this week how iterators work. He 
explained how to create them and how to use them.

The following function achieves a goal by explicitly using an iterator. 
Examine it carefully:

def main(list_in):
    iterator = iter(list_in)
    list_out = []
    while True:
        try:   
            list_out.append(next(iterator) * 2)
        except StopIteration:
            break
    return list_out         

In this exercise, we'd like you to completely rewrite the 'main' function above 
by omitting the iterator and using either a for-loop or a list comprehension 
instead.

Your own function should also be called 'main' and should achieve the same
goal as the one above.
"""

#lst= ['1','2','3','4']
def main(list_in):
    list_out = []
    for i in list_in:
        list_out.append(i*2)
    

    return list_out
