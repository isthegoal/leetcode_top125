# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：请判断一个链表是否为回文链表。

            示例 1:
            输入: 1->2
            输出: false

            示例 2:
            输入: 1->2->2->1
            输出: true

      最佳是使用O(n) 时间复杂度和 O(1) 空间复杂度解决问题。

      分析：


      思路：  有下面两种解法方式，
            【1】解法一，空间占用较大的方式，
            【2】解法二, 空间复杂度为O(1)的方式.可以设置快慢指针，当快指针走完时，慢指针刚好走到中点，
            随即原地将后半段反转。然后进行回文判断。

'''
#解法一
class Solution1:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        l = []
        p = head
        while p.next:
            l.append(p.val)
            p = p.next
        l.append(p.val)
        return l == l[::-1]

#解法二
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val
        fast = slow = q = head
        while fast.next and fast.next.next:#这里快指针的判读条件跟判断环形有一点不同
            fast = fast.next.next
            slow = slow.next
        def reverse_list(head):
            if head is None:
                return head
            cur = head
            pre = None
            nxt = cur.next
            while nxt:
                cur.next = pre
                pre = cur
                cur = nxt
                nxt = nxt.next
            cur.next = pre
            return cur
        p = reverse_list(slow.next)
        while p.next:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return p.val == q.val

#################    另一种非常容易直观理解的 快慢指针法    ##################
class Solution(object):
    def isPalindrome(self, head):
        if not head:
            return True
        fast = slow = head
        # 快指针指向下两个，这样遍历之后，slow只走到中间节点
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next

        # 将中间节点之后的链表反转
        p, rev = slow, None
        while p:
            rev, rev.next, p = p, rev, p.next

        # 重新以head开始比较反转后的链表
        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True
#___________________________________    练习1   ______________________________#
'''
     基本思路非常简单，就是三步吧，主要针对于回文  链表的性质 使用快慢指针法 做处理。
         回文其实 是一种可以在中间位置 产生对称形式的链表。
      （1）这里是设定快慢两个指针，快指针每次走两步，慢指针每次走一步。
      （2）当  快指针走到头时，因为慢指针时间慢一倍，所以其肯定是走到了半中间的位置。
      （3）此时 如果回文情况下，快慢指针的指向应该是 顺序刚好相反的，因此可以将慢指针指向之后的顺序倒过来 
            从  1-2-3-3-2-1 翻转成1-2-3-1-2-3。
      （4） 此时一个从1开始，一个从1-2-3-1开始  进行比较，如果能让后面那个走到头，说明是成功的回文链表。
      
      
    关于 第三步 有个多值同时赋值的问题，可以参考这个：https://blog.csdn.net/u011320646/article/details/17843227
    
    像这种 比较长的同时赋值，是一种无记忆的 从左往右的赋值方式。
        a=2
        b=3
        c=6
        a,b,a=4,a,c
        print(b)       结果 b是2， a是6 
    
    而这里rev,rev.next,p=p,rev,p.next 是经典的 单步完成三行的，对链表进行逆置的方程式。 p是实际载有的，rev是中间变量。
                        tmp = cur.next
                        cur.next = p
                        p = cur
                        cur = tmp

'''
def fun1(head):
    # 边界
    if not head:
        return True
    #  第一步.创建快慢链表吧
    slow=fast=head

    # 第二步，两个一起走，快的一次走两步(走不成两步就走一步)，直到快的到头
    while fast:
        slow=slow.next
        #  这个必须得有  if fast.next else fast.next 这段，否则行不通，先走单步上的判别才行
        fast=fast.next.next if fast.next else fast.next

    # 第三步，是不好理解的地方   从slow位置开始翻转
    p,rev=fast,None
    while p:
        # 这句话 实现了后半段链表的翻转，而且还没断链？？？  这么牛的吗   可以实现把，算是，同时赋值，是一种无记忆的  从左往右。
        # 好吧，  链表的逆置，画一下就能看出来了。  再理解下翻转的过程吧
        rev,rev.next,p=p,rev,p.next

    #第四步，很顺理成章的，进行从两个位置开始后的逐个比较即可.    rev是从中间开始的
    while rev:
        if rev.val!=head.val:
            return False

        rev=rev.next
        head=head.next

    return True
