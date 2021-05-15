"""
Write a function called 'main' that accepts a string consisting of lowercase 
letters as an argument.

Your function should return a string with the same characters as in the
input string. Except, when a character is present in the list: ['b', 'c', 'd'],
then the second occurence of that character should be capitalized.

You can be sure that all the characters in the input string have two or more 
occurences.  

Hint: try to solve the problem using only the replace method of strings (and 
some creativity).

For example:
If we are calling your function as:
main('becabfdceecadacffefbada') 
then it should return the string: 
'becaBfdCeecaDacffefbada'
"""
# good version

# def main(x):
#       for i in ['b','c','d']:
#             x = x.replace(i, i.upper(), 2)
#             x = x.replace(i.upper(), i, 1)

#       return x
# main('becaBfdCeecaDacffefbada')


# nogada version
def main(txt):
      
      b_new_L = txt[:txt.find('b', txt.find('b')+1 )] 
      b_new   = 'B'
      b_new_R = txt[txt.find('b', txt.find('b')+1 )+1:] 

      b_replaced = b_new_L + b_new + b_new_R

      c_new_L = b_replaced[:b_replaced.find('c', b_replaced.find('c')+1 )] 
      c_new   = 'C'
      c_new_R = b_replaced[b_replaced.find('c', b_replaced.find('c')+1 )+1:] 

      c_replaced = c_new_L + c_new  + c_new_R

      d_new_L = c_replaced[:c_replaced.find('d', c_replaced.find('d')+1 )] 
      d_new   = 'D'
      d_new_R = c_replaced[c_replaced.find('d', c_replaced.find('d')+1 )+1:] 

      d_replaced = d_new_L + d_new + d_new_R

      return d_replaced 

#main('becabfdceecadacffefbada')





# for i in txt:
#       txt.find('b', txt.find('b')+1 )
#       txt.find('c', txt.find('c')+1 )
#       txt.find('d', txt.find('d')+1 )


# count_b = 0
# count_c = 0
# count_d = 0

# for index in range(len(txt)):
      
#       if   txt[index] == 'b':
#             count_b += 1
#       elif txt[index] == 'c':
#             count_c += 1
#       elif txt[index] == 'd':
#             count_d += 1

#       if count_b == 2:
#             txt.replace('b','B', index)
#       if count_c == 2:
#             txt[index] = 'C'
#       if count_d == 2:
#             txt[index] = 'D'
            
# print(txt)



      









# def processString5(txt):
#   transTable = txt.maketrans("bcd", "BCD")
#   txt = txt.translate(transTable)
#   print(txt)
# processString5(txt) 



# translate()와maketrans()는 정규식 이외의 다른 접근 방식을 사용하며 사전을 사용하여 이전 값을 새 값으로 매핑합니다.

# maketrans()는 3 개의 매개 변수 또는 단일 매핑 사전을 허용합니다.

# str1-대체 할 문자열
# str2-위의 문자를 대체하는 문자열
# str3-삭제할 문자열
# maketrans()는 원래 문자열과 대체 문자열 간의 매핑 테이블입니다.

# translate()는maketrans()가 반환하는 모든 것을 수락하고 번역 된 문자열을 생성합니다.

# 문자열 내의 모든 소문자 모음을 대문자로 변환하고 문자열에서 발견 된 모든 x, y, z를 삭제한다고 가정 해 보겠습니다.

# txt = "Hi, my name is Mary. I like zebras and xylophones."

# def processString5(txt):
#   transTable = txt.maketrans("aeiou", "AEIOU", "xyz")
#   txt = txt.translate(transTable)
#   print(txt)
  
# processString5(txt)