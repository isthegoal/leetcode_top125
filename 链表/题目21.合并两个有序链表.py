# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
            示例：
            输入：1->2->4, 1->3->4
            输出：1->1->2->3->4->4

      分析：

      思路：先声明一个newhead作为dummy head，最后返回它的next作为答案，然后对于l1, l2线性扫描，每次选两者中值小的那个作为新链表的下一个节点，
      然后选取的链表前进一步。如果l1, l2里有一个已经结束了，就把另一个剩下的值全部直接连过来。

      建立一个新链表，遍历即可。

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(0)
        p = newhead
        while (l1 and l2):
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next

        if l1:
            p.next = l1
        else:
            p.next = l2
        return newhead.next
#___________________________________    练习1   ______________________________#
'''
    比较简单的 一道题，直接按照大小关系进行 比较并合并即可.
        新创建L3(newhead):
        (1)如果L1,L2都存在，进行循环；对L1,L2节点依次比较大小，较小的存入L3；
           *若L1较小，L1存入L3[就是将val存到L3中]，L1节点后移；
           *若L2较小，L2存入L3，L2节点后移；
        (2)当若L1, L2有一个不存在，则将后续节点全部赋值给L3；

'''

def fun1(l1,l2):
    # 首先要新创建一个链表
    newhead=ListNode(0)
    p=newhead

    # 开始按照第一步的方式  不断比较加入吧。  满足第一步的条件
    while(l1 and l2):
        #若L1较小，L1存入L3
        if l1.val<l2.val:
            p.next=ListNode(l1.val)
            l1=l1.next
        #若L2较小，L2存入L3，L2节点后移
        else:
            p.next = ListNode(l2.val)
            l2 = l2.next

    # 第二步，对于余下的做统一处理即可
    if l1:
        p.next=l1
    else:
        p.next=l2

    # 最后返回合并的结果即可
    return newhead.next

