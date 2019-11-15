# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/17677
'''

import re

def solution(str1, str2):
    r = re.compile(r'[\W\d_]')

    re_str1 = str1.lower()
    re_str2 = str2.lower()
    
    set_str1 = [re_str1[i]+re_str1[i+1] for i in range(len(re_str1)-1) if not r.search(re_str1[i]+re_str1[i+1])]
    set_str2 = [re_str2[i]+re_str2[i+1] for i in range(len(re_str2)-1) if not r.search(re_str2[i]+re_str2[i+1])]
    
    cnt = 0
    for x in set_str1:
        if x in set_str2:
            cnt += 1
            set_str2.remove(x)
            
    try :
        answer = int(cnt/(len(set_str1)+len(set_str2))*65536)    
        return answer
    except ZeroDivisionError as e:
        #print(e)
        return 65536


if __name__ == '__main__':
#    str1, str2 = 'FRANCE', 'french' # 16384
#    str1, str2 = 'handshake', 'shake hands' # 65536
#    str1, str2 = 'aa1+aa2', 'AAAA12' # 43690
    str1, str2 = 'E=M*C^2', 'e=m*c^2' # 65536
    
    print(solution(str1, str2))
    