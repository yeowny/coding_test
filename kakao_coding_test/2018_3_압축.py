# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/17684
'''

def solution(msg):
    word_dict = {chr(65+xx): xx+1 for xx in range(26)}

    i = 0
    answer = []
    while i != len(msg):
        j = 1
        while i+j-1 != len(msg):
            if not word_dict.get(msg[i:i+j]):
                answer.append(word_dict.get(msg[i:i+j-1]))
                word_dict[msg[i:i+j]] = len(word_dict)+1
                break
            j += 1
        i += j-1
    answer.append(word_dict.get(msg[i-j+1:]))

    return answer


if __name__ == '__main__':
#    msg = 'KAKAO' # [11, 1, 27, 15]
#    msg = 'TOBEORNOTTOBEORTOBEORNOT' # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
    msg = 'ABABABABABABABAB' # [1, 2, 27, 29, 28, 31, 30]
    
    print(solution(msg))
