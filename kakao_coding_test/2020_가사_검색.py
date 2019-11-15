# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/60060
'''
        
class Trie:
    def __init__(self):
        self.cnt = 0
        self.children = {}
        
    def insert(self, word):
        curr_node = self
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = Trie()

            curr_node = curr_node.children[c]
            curr_node.cnt += 1
    
    def search_count(self, word):
        curr_node = self
        for c in word:
            if c not in curr_node.children:
                return 0
            
            curr_node = curr_node.children[c]
        
        return curr_node.cnt
        
def solution(words, queries):
    forward_trie = Trie()
    backward_trie = Trie()
    for w in words:
        forward_trie.insert(str(len(w))+w)
        backward_trie.insert(str(len(w))+w[::-1])
    
    answer = []
    for q in queries:
        if q[0] != '?':
            answer.append(forward_trie.search_count(str(len(q))+q.replace('?','')))
        else:
            answer.append(backward_trie.search_count(str(len(q))+q.replace('?','')[::-1]))
    
    return answer


if __name__ == '__main__':
    words, queries = ["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"] # [3, 2, 4, 1, 0]

    print(solution(words, queries))
