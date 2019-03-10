# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:45:54 2019

@author: 2010
"""

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        lenth=len(s)
        sr=''
        for i in range(lenth):
           if s[i]==' ':
              sr+='%20'
           else:
               sr+=s[i]
        return sr
if __name__=='__main__':
    a=Solution()
    s='We Are Happy'
    b=a.replaceSpace(s)
    print(b)
    
        