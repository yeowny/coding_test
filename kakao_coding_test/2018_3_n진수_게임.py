# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/17687
'''

def fn_num(x, n):
    result = []

    s_i = 0
    while True:
        s_i += 1
        if x < n**s_i:
            s_i -= 1
            break

    for i in range(s_i, -1, -1):
        j = 0
        while True: 
            j += 1
            if x < j*n**i:
                j -= 1
                x -= j*n**i
                if j < 10:
                    result.append(str(j))
                else:
                    result.append(chr(55+j))
                break
    return result

def solution(n, t, m, p):
    x = 0
    result_list = []
    while len(result_list) < ((t-1)*m + p):
        result_list.extend(fn_num(x, n))
        x += 1

    return ''.join([result_list[xx] for xx in [p-1+yy for yy in range(0, t*m, m)]])


if __name__ == '__main__':
#    n, t, m, p = 2, 4, 2, 1 # 0111
#    n, t, m, p = 16, 16, 2, 1 # 02468ACE11111111
    n, t, m, p = 16, 16, 2, 2 # 13579BDF01234567
    
    print(solution(n, t, m, p))
