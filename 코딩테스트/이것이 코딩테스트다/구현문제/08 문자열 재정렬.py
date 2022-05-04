input = 'K1KA5CB7'

# print(sorted(list(input)))
# print(sorted(['K', '1', 'K', 'A', '5', 'C', 'B', '7']))
numbers = [4, 2, 12, 8]

sorted_numbers = sorted(input)
print(sorted_numbers)

answer_str = ''
answer_int = ''
for i in sorted_numbers :
    print(i)
    if type(i) == int:
        answer_int += str(i)
    else:
        answer_str += i
answer = answer_int + answer_str 

print(answer)

# isalpha
# ''.join()
# result.sort()