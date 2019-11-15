# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/60058
'''

def check_p(p):
    while '()' in p:
        p = p.replace('()', '', len(p)//2)
    
    return True if len(p)==0 else False

def split_p(p):
    l, r = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        else:
            r += 1
            
        if l==r: 
            return p[:i+1], p[i+1:]
    
def solution(p, answer=''):
    if check_p(p):
        return answer+p
    
    u, v = split_p(p)
    if check_p(u):
        answer = solution(v, answer+u)
    else:
        answer = solution(v, answer+'(') + ')'
        for x in u[1:-1]:
            answer += '(' if x==')' else ')'
    
    return answer


if __name__ == '__main__':
#    p = "(()())()" # "(()())()"
#    p = ")(" # "()"
    p = "()))((()" # "()(())()"

    print(solution(p))
