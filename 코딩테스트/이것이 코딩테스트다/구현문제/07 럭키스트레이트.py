num = 7755
front_num = 0
after_num = 0

for i in range(len(str(num))):
    if i < len(str(num))//2:
        front_num += int(str(num)[i])
    else:
        after_num += int(str(num)[i])
if front_num == after_num:
    print('LUCKY')
else:
    print('READY')



# front = 