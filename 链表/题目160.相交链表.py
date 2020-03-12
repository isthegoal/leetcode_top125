# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：编写一个程序，找到两个单链表相交的起始节点。

         示例 1：
            输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
            输出：Reference of the node with value = 8
            输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，
            链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，
            相交节点前有 3 个节点。


      分析：


      思路：题目比较简单吧，有两种思路。
           【1】把链表A里的每一个节点都在链表B里查找，时间复杂度O(MN)，空间复杂度O(1)
           【2】把链表A里的每个节点都记录在哈希表里，然后遍历链表B，返回第一个出现在哈希表里的节点。
                时间复杂度O(M + N)，空间复杂度O(M)
           【3】先分别找出两个链表的长度la, lb, 这样就可以知道二者长度的差值la - lb，然后让较长的那个链表先走la - lb步，
            然后两个链表一起每次走一步，第一次相遇的那个节点就是交点。时间复杂度O(M + N)

'''

#  方式二的解法
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dic = {}
        p = headA
        while p:
            dic[p] = 1
            p = p.next
        p = headB
        while p:
            if p in dic:
                return p
            p = p.next
        return None

# 方式三的解法
class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa, pb = headA, headB
        la, lb = 0, 0
        while pa:
            la += 1
            pa = pa.next

        while pb:
            lb += 1
            pb = pb.next

        if la < lb:
            la, lb, headA, headB = lb, la, headB, headA

        n = la - lb
        pa, pb = headA, headB
        while n:
            pa = pa.next
            n -= 1

        while pa:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None

#___________________________________    练习1   ______________________________#
# 题意 非常的简单， 从leetcode中的题目给的图 理解题意是更为直观的，就是   两个链表从一个位置开始 后续的链段是重合的，需要 找到这个重合的起点位置。

def fun1(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    评论区一个很巧妙的方法，使两个链表到达相等位置时走过的是相同的距离。

       因为：链表1的长度是x1+y，链表2的长度是x2+y，
       所以方法：我们同时遍历链表1和链表2，到达末尾时，再指向另一个链表。则当两链表走到相等的位置时：x1+y+x2 = x2+y+x1
    """
    p = headA
    q = headB
    # 不断进行遍历，通过附加，使得 链表到达相等位置时走过的是相同的距离  （下面的if  else操作值得品味）
    while p != q:
        #  这里会变成 x1 -> x1+y -> x1+y+x2 ->x1+y+x2+y   (其中x1是L1区别于L2的部分，x2同理，对比下来发现了吧，经过等长之后，就会到达y的区域，然后就重合了，ok.)
        p = p.next if p else headB
        #  这里会变成 x2 -> x2+y -> x2+y+x1 ->x2+y+x1+y
        q = q.next if q else headA

    # 最后p指向的位置，就是重合开始的位置。
    return p