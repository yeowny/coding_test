# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/17681
'''

def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        tmp_answer = ''
        for x, y in zip([bool(int(xx)) for xx in str(bin(a1))[2:].zfill(n)], [bool(int(xx)) for xx in str(bin(a2))[2:].zfill(n)]):
            tmp_answer += '#' if x or y else ' '
        answer.append(tmp_answer)

    return answer


if __name__ == '__main__':
#    n, arr1, arr2 = 5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28] # ["#####","# # #", "### #", "# ##", "#####"]
    n, arr1, arr2 = 6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10] # ["######", "### #", "## ##", " #### ", " #####", "### # "]
    
    print(solution(n, arr1, arr2))
