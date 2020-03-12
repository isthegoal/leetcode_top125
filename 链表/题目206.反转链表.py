# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：反转一个单链表。

      示例:
        输入: 1->2->3->4->5->NULL
        输出: 5->4->3->2->1->NULL

      分析：


      思路：   这个是非常经典的问题，有好几种思路吧，包括
          【1】递归法。假设我们已经得到了把head.next翻转完成的结果，p指向这个结果的头，head的next指针此时指向这个
          结果的最后一个节点，即head.next。为了将head也翻转，我们需要让head.next的next指针指向head，然后把head的next置空，
            最后返回p即可。
          【2】利用栈先进后出的性质。将所有节点压入栈，然后逐个弹出连接next指针。
          【3】迭代法。
'''

#  方法一，迭代的方式
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

#  方法二，栈的方式
class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next

        newhead = stack[-1]
        p = newhead
        stack.pop()
        while stack:
            p.next = stack.pop()
            p = p.next

        p.next = None
        return newhead

#  方法三，迭代的方式
class Solution3(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            tmp = cur.next #保存尾部
            cur.next = pre #逆转局部
            pre = cur #pre后移
            cur = tmp #cur后移
        return pre

#___________________________________    练习1   ______________________________#
#  这里使用 栈 先进后出的性质，将所有节点压入栈，然后逐个弹出并连接next指针

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 边界条件 如果 链表为空
        if not head or not head.next:
            return head

        # 栈的创建与附加。  将链表元素 如栈
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next

        #  弹出栈，并拼接出新的链表. 新创建的链表也用p指针指向
        newhead = stack[-1]
        p = newhead
        stack.pop()

        # 开始正式的拼进去到 p中
        while stack:
            p.next = stack.pop()
            p = p.next

        p.next = None
        return newhead