# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 21:00:08 2019

@author: 2010
"""

class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
class LinkedList():
    def __init__(self,ListNode=None):
        self.head=ListNode
        self.length=0
    def append(self, this_node):
         
         this_node = ListNode(this_node) 
         if self.is_empty(): 
             self.head = this_node 
         else: 
             p = self.head 
             while p.next!=None: 
                  p = p.next
             p.next = this_node 
         self.length+=1
    
    def appendNode(self, node):
        if self.is_empty():
            self.head = node
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = node
        self.length += 1

    def is_empty(self):
        return self.head==None
    def Length(self):
        count=0
        cur=self.head
        while cur!=None:
            count+=1
            cur=cur.next
        return count
            
            
    def PrintList(self):
        cur=self.head
        res=[]
        while cur!=None:
            res.append(cur.val)
            cur=cur.next
        print(res[::-1])
    def FindKthToTail(self, k):
        # write code here
        length=0
        cur=self.head
        while cur!=None:
            length+=1
            cur=cur.next
        if not 0<=k<length:
            return 'Error'
        i=0
        p=self.head
        q=self.head
        if i<k:
            p=p.next
            
            i+=1
        while i>=k and p!=None:
            q=q.next 
            p=p.next
       
        print(q.val)
        return q.val
  
if __name__=='__main__':
   #a=ListNode(1)
    #b=ListNode(2)
    #c=ListNode(3)
    s=LinkedList()
   
    
    s.append(1) 
    
    b=ListNode(2)
    
#    s.append(b) 
#// 仔细看一下你的append函数参数，
#   b是一个ListNode对象，
#    你append的参数是一个ListNode对象的val
    
    c=ListNode(3)
    
    s.appendNode(b)
    s.appendNode(c)

#    s.append(c)
    print(s.is_empty())
    
    s.PrintList()
    print(s.FindKthToTail(1))
            
        
