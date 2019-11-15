# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/17682
'''

def solution(dartResult):
    dartResult = dartResult.replace('10', '_')
    tmp_dict = {'S': 1, 'D': 2, 'T': 3}
    
    answer = []
    for x in dartResult:
        if x == '_':
            answer.append(10)
        elif x.isdigit():
            answer.append(int(x))
        else:
            if x == '#':
                answer[-1] *= -1
            elif x == '*':
                answer[-1] *= 2
                if len(answer) != 1:
                    answer[-2] *= 2
            else:
                answer[-1] **= tmp_dict[x]
    return sum(answer)


if __name__ == '__main__':
#    dartResult = '1S2D*3T' # 37
#    dartResult = '1D2S#10S' # 9
#    dartResult = '1D2S0T' # 3
#    dartResult = '1S*2T*3S' # 23
#    dartResult = '1D#2S*3S' # 5
#    dartResult = '1T2D3D#' # -4
    dartResult = '1D2S3T*' # 59
    
    print(solution(dartResult))
