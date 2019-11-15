# -*- coding: utf-8 -*-

# =============================================================================
# @author: yeowny
# woon young, YEO
# ywy317391@gmail.com
# https://github.com/yeowny
# =============================================================================

'''
https://programmers.co.kr/learn/courses/30/lessons/42892
'''

import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = self.right = None


def preorder(tree, result=[]):
    if tree != None:
        result.append(tree.idx)
        preorder(tree.left, result)
        preorder(tree.right, result)
    return result

def inorder(tree, result=[]):
    if tree != None:
        inorder(tree.left, result)
        result.append(tree.idx)
        inorder(tree.right, result)
    return result

def postorder(tree, result=[]):
    if tree != None:
        postorder(tree.left, result)
        postorder(tree.right, result)
        result.append(tree.idx)
    return result


def solution(nodeinfo):
    nodeinfo_idx = sorted([xx+[ii+1] for ii, xx in enumerate(nodeinfo)], key=lambda x: -x[1])
    
    tree = Tree(*nodeinfo_idx[0])
    tmp_tree = tree
    for node in nodeinfo_idx[1:]:
        new_tree = Tree(*node)
        while True:
            if new_tree.x < tmp_tree.x:
                if tmp_tree.left != None: 
                    tmp_tree = tmp_tree.left
                else:
                    tmp_tree.left = new_tree
                    tmp_tree = tree
                    break
            else:
                if tmp_tree.right != None: 
                    tmp_tree = tmp_tree.right
                else:
                    tmp_tree.right = new_tree
                    tmp_tree = tree
                    break
    
    return [preorder(tree), postorder(tree)]


if __name__ == '__main__':
    nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]] # [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
    
    print(solution(nodeinfo))
