# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

            给定一个链表: 1->2->3->4->5, 和 n = 2.
            当删除了倒数第二个节点后，链表变为 1->2->3->5.

      分析：

      思路：有多种思路。
          （1）链表转list处理再转链表输出。
          （2）一趟扫描获得链表长度l，然后删除从前往后的第l - n +1个节点。
          （3）快慢指针法，快指针先走n步，然后快慢指针一起走，当快指针是链表尾部的最后一个元素时，慢指针指向元素的下一个元素就是需要删的那个元素。
'''

#  快慢指针法
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        slow, fast = p, p
        while (n):
            n -= 1
            fast = fast.next
        if fast is None:
            return p.next
        while (fast and fast.next):
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return p

#___________________________________    练习1   ______________________________#
# 这道题是十分简单的， 主要还是针对于  链表无法索引的问题 ，寻找合适的方式高效的做内部操作。
#  这里的想法  是使用经典的快慢指针法就行，保持间隔，并让一个指针先到终点。        先走n步，从而可以有效的找到需删除位置。

def remove_nth(head,n):
    '''
    :param head:  链表头指针
    :param n:     所指到的倒数第几个位置
    :return:
    '''
    # 首先初始创建  双 快慢指针
    p=head
    slow,fast=p,p

    # 设定p和q之前的快慢指针间隔
    while(n):
        n-=1
        fast=fast.next

    # 进行fast 是否初始就到头的判别
    if fast is None:
        return p.next

    # 进行重要的 按照快慢指针情况的行走
    while(fast and fast.next):
        fast=fast.next
        slow=slow.next

    # 最后找到位置，进行删除即可  ，完成删除操作就搞定所有吧。
    slow.next=slow.next.next

    return p

