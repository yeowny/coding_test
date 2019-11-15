# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/60057
'''

def split_text(s):
    result = []
    len_text = len(s)
    for i in range(1, len_text//2+1):
        result.append([s[j:min(j+i, len_text)] for j in range(0, len_text, i)])
        
    return result

def solution(s):
    answer = [len(s)]
    for x in split_text(s):
        tmp_token, tmp_answer = '', []
        x += [None]
        for i in range(len(x)-1):
            if x[i] != x[i+1]:
                tmp_token = ''
                tmp_answer.append(x[i])
            else:
                if tmp_token == x[i]:
                    tmp_answer[-1] += 1
                else:
                    tmp_token = x[i]
                    tmp_answer.append(2)
        answer.append(len(''.join([str(xx) for xx in tmp_answer])))
    return min(answer)


if __name__ == '__main__':
#    s = "aabbaccc" # 7
#    s = "ababcdcdababcdcd" # 9
#    s = "abcabcdede" # 8
#    s = "abcabcabcabcdededededede" # 14
    s = "xababcdcdababcdcd" # 17
    
    print(solution(s))
