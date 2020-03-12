# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
      为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
      如果 pos 是 -1，则在该链表中没有环。

          示例 1：
            输入：head = [3,2,0,-4], pos = 1
            输出：tail connects to node index 1
            解释：链表中有一个环，其尾部连接到第二个节点。

          示例 2：

            输入：head = [1], pos = -1
            输出：no cycle
            解释：链表中没有环

      分析：


     思路：快慢指针法。先判断链表有没有环，如果链表有环，则让快指针回到链表的头重新出发，当快慢指针相遇的那个节点即是
     链表环的起点。

     思路非常简单，就是三步，也是在  题目141快慢指针基础上再加一步。
     （1）快慢指针走，  直到快慢指针碰头。   一个每次走两步，一个每次走一步。
     （2）重新一个指针从碰头位置走、一个从起点走，都每次走一步，  当这两个行走再碰头时，位置点就是 环的入点。

     至于 为什么第二步能行，能可以看图和推导出来，先可以记住这种方式。  一点解释:

            第一个慢指针走过的路程长度是x1 + x2 + k1 * (x2 + x3)。
            第二个快指针走过的路程长度是x1 + x2 + k2 * (x2 + x3)。
            由快慢指针的速度关系得：(x1 + x2) * 2 + 2 * k1 * (x2 + x3) = x1 + x2 + k2 * (x2 + x3)，
            因此x1 + x2 = (k2 - 2 * k1) * (x2 + x3)，进而有x1 - x3 = (k2 - 2 * k1 - 1) * (x2 + x3)。
            这说明x1和x3的距离差值刚好是环长(x2 + x3)的整数倍。因此，我们只需令其中一个指针指向虚拟头节点，
            而另一个指针则仍然在相遇的那个节点，一起移动这两个指针，直到这两个指针相遇，这个新的相遇点就是链表开始入环的第一个节点。


'''

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #边界条件 判别
        if not head or not head.next:
            return None
        #  (1)跟  141一样的，快慢指针法，如果快慢指针会和，那就是有环。
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

            if slow == fast:
                break
        # 小过程吧，没环就可以退出了。
        if slow != fast:  # 链表无环
            return None

        #  (2)主要的地方，在确定有环后，   分别从fast与slow相遇点 、起点  开始走，两者每次走一步，当再次走到重合点，那就是 链表入环点，很经典的思路。
        fast = head
        while slow:
            if slow == fast:  # 此点即是环起点
                return slow
            slow = slow.next
            fast = fast.next

#___________________________________    练习1   ______________________________#
'''
     说曹操，曹操到，我141题还在纳闷来，为什么只是判断是否是 链表，而没有 让找 链表的环位置。
     
     这题就刚好，让找到这个环的入点位置。以前做过这道题，很经典的思路吧，进行了两次走 即可。

'''
def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    #边界条件 判别
    if not head or not head.next:
        return None
    #  (1)跟  141一样的，快慢指针法，如果快慢指针会和，那就是有环。
    slow, fast = head, head
    while fast:
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next

        if slow == fast:
            break
    # 小过程吧，没环就可以退出了。
    if slow != fast:  # 链表无环
        return None

    #  (2)主要的地方，在确定有环后，   分别从fast与slow相遇点 、起点  开始走，两者每次走一步，当再次走到重合点，那就是 链表入环点，很经典的思路。
    fast = head
    while slow:
        if slow == fast:  # 此点即是环起点
            return slow
        slow = slow.next
        fast = fast.next
