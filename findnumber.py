# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:27:01 2019

@author: 2010
"""

class Solution:
    # array 二维列表
    def insert2dArray(self, seq, row, col):
        # 没有使用numpy的array
        # array = [[0] * col] * row 这种方式是浅拷贝，不好用
        array = [[0 for i in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                array[i][j] = seq[i * row + j]
        return array

    def Find(self, target, array):
        # 主要思路：首先选取右上角的数字，如果该数字大于target，则该列全大于target，删除该列；
        # 如果该数字小于小于target，则该列全小于target，删除该行。
        found = False
        row = len(array)
        if row:
            col = len(array[0])
        else:
            col = 0

        if row > 0 and col > 0:
            # find index of top right-hand corner
            i = 0
            j = col - 1
            # if never meets lower-left corner
            while i < row and j >= 0:
                if array[i][j] == target:
                    found = True
                    # forget break
                    break
                elif array[i][j] > target:
                    j -= 1
                elif array[i][j] < target:
                    i += 1
        return found

if __name__ == '__main__':
    answer = Solution()
    seq = [1, 2, 8, 9, 2, 4, 9, 12, 4, 7, 10, 13, 6, 8, 11, 15]
    matrix = answer.insert2dArray(seq, 4, 4)
    print(matrix)
    print(answer.Find(7, matrix))
#if __name__ == '__main__':
   # s=Solution()
    # target=[1,3,4]
    #flag=s.Find(target,array)
    #print(flag)
    
#while True:
    
    #try:
     #   s = Solution()
       # L = list(eval(raw_input())
        #array = L[1]   ###二维数组
        #target = L[0]  ###目标数
        #print(s.Find(target,array)
    #except:
       # break
#