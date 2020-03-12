'''
    题目：

        给定一个链表，判断链表中是否有环。
        为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

        示例 1：
            输入：head = [3,2,0,-4], pos = 1
            输出：true
            解释：链表中有一个环，其尾部连接到第二个节点。

        示例 2：
            输入：head = [1,2], pos = 0
            输出：true
            解释：链表中有一个环，其尾部连接到第一个节点。

        示例 3：
            输入：head = [1], pos = -1
            输出：false
            解释：链表中没有环。

        这个题目让我迷糊了一阵，其中：
                pos是给官方代码生成环形链表的
                生成后的链表即代码模版中的head
        所以只需要判断这个链表是否环形。那就是很简单的  环指向的问题。 传统的判别的思路即可


    思路：
        非常简单和经典的一道题，我觉得直接  异或，利用位运算就解出来了，感觉是剑指的原题。           要求不用空间，时间复杂度为O(N)

        这里有两种思路吧，一种是 使用快慢指针的方式，另一种则是使用下面的哈希标记的方法。

    方法：

'''

#思路  是一种比较另类的 哈希法，就是对走过的添加标记， 之后发现如果再走到这个标记，则是环。
def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head:
        return False

    # 遍历的过程中将值置空 (置空法，所有行走时把 当前位置置空)      这里注意head.val是个关键，当前为空时有两种可能，一种是非环，另一种就是本身是环，但是却被自己置空了，思路非常清奇。
    while head.next and head.val != None:
        head.val = None
        head = head.next

    # 如果   head.val==None，且next无指向时，说明 不是环
    if not head.next:
        return False

    # 如果   head.val==None，但是next有指向时，说明 val是被强制置空的，则这是环
    return True

#___________________________________    练习1   ______________________________#
# 这里先使用，非常经典的  用于环形判别的快慢指针法吧，good
#  使用快慢指针方法 可以用于 判别是否有环，或者找到构成环的结点，其中 单纯判别环更简单些，就是如下的方式。
def fun1(head):
    #  边界条件判别
    if not head or not head.next:
        return False

    # 创建快慢指针吧
    slow,fast=head,head

    # 进行快慢指针的行走，注意 快指针是每次走两步，慢指针每次走一步，进行判别即可。
    while fast:

        slow=slow.next
        fast=fast.next

        if fast:
            fast=fast.next
        # 进行产生重复位置的判别。核心的 如果有环，快慢指针必定会产生重叠的
        if slow==fast:
            return True

    #  如果不会碰头，那fast走完了，就没有环
    return False

#___________________________________    练习2   ______________________________#
# 这个是哈希字典标记法，标记来判别是否 有环情况，相当更简单。    构建个标记。
def fun2(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    record = dict()

    p = head
    while p:
        # 如果之前走过的数值，就标记为1，说明以前走过了
        if p not in record:
            record[p] = 1
        #重要的，如果 已经出现过，但是又走了，那就产生环了呗.....
        else:
            return True
        p = p.next
    return False
