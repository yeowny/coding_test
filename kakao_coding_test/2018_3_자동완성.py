# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/17685
'''

def fn_1(x, y):
    cnt = 0
    for i in range(min(len(x), len(y))):
        if x[i] == y[i]:
            cnt += 1
        else:
            break
    return cnt+1

def solution(words):
    words = ['_'] + sorted(words) + ['_']
    answer = 0
    for i in range(1, len(words)-1):
        answer += min(len(words[i]), max(fn_1(words[i-1], words[i]), fn_1(words[i], words[i+1])))

    return answer


if __name__ == '__main__':
#    words = ['go','gone','guild'] # 7
#    words = ['abc','def','ghi','jklm'] # 4
    words = ['word','war','warrior','world'] # 15
    
    print(solution(words))
