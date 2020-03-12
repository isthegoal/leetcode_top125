# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

        示例 1：
        输入: 4->2->1->3
        输出: 1->2->3->4

        示例 2:
        输入: -1->5->3->4->0
        输出: -1->0->3->4->5

      分析：
           这就可以用归并 或者 快速排序解决， 只不过处理的是链表，会比处理数组麻烦点。
                   就比如找中点 和 链表合并的过程更为复杂一些。

      思路：  （归并排序的思路）
        递归排序，
        1. 找中点，把链表一分为二
        2. 递归处理左右半边
        3. 合并排好序的部分

      递归归并排序的方式，时间复杂度是 O(nlog(n))，空间复杂度为O(N)，就是最普通的  归并排序的思想，只不过是排序链表。

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #####   第一步.找中点的过程，使用了快慢指针。  #####
        if not head or not head.next:
            return head
        pre, slow, fast = head, head, head
        while fast and fast.next:  # 找链表中点
            pre = slow
            slow = slow.next
            fast = fast.next.next

        # 现在  slow实际指向的是中点，  接下里 递归处理左右半边。   （这里因为归并排序的方式，其实默认在递归由下往上的过程中，left和right已经是排好序的了）
        pre.next = None
        left, right = self.sortList(head), self.sortList(slow)

        #针对分值的 细小部分， 使用 merge函数 进行比较排序合并，合并成有序链表序列。
        return self.merge(left, right)

    #  函数的作用，就是使用递归的方式，将L1和L2按照大小关系合并成L3的算法过程。  很普通的递归合并链表算法。
    def merge(self, l1, l2):
        #  下面  归并排序中，细微的按照 l1和l2关系 进行合并的过程。

        # 边界条件
        if not l1:
            return l2
        if not l2:
            return l1

        # 针对 l1和l2比较长的序列，进行逐项的合并，下面的过程就是合并的，一种递归的  将L1和L2元素按照大小关系从小到大合并到一起的方法。
        if l1.val < l2.val:
            head = ListNode(l1.val)
            head.next = self.merge(l1.next, l2)
        else:
            head = ListNode(l2.val)
            head.next = self.merge(l1, l2.next)

        #
        return head

#  可以使用 快速排序 或者  归并排序的方式，下面是 快速排序的写法

#___________________________________    练习1   ______________________________#
'''
     使用了由  小块往大块的合并过程，  sortlist负责块的分离和组织， merge负责块的按大小上的合并计算。
'''
# 控制 归并排序的 分离和主控制循环函数。  块控制
def sortlist(head):
    # 边界
    if not head or not head.next:
        return head
    #  首先找到中间位置，  特有的针对链表，使用快慢指针法找到中间位置
    pre, slow, fast = head, head, head
    while fast and fast.next:  # 找链表中点
        pre = slow
        slow = slow.next
        fast = fast.next.next

    # 找到中点后，递归排序 分离的两端
    pre.next = None
    left, right = sortlist(head), sortlist(slow)

    # 最后获取合并的结果，进行返回。
    return merge(left, right)

#  类似于快排的 partation一样，这里是排序的主要过程的体现，    进行块内排序
def merge(l1, l2):
    # 边界条件  (块归并的 边界信息)
    if not l1:
        return l2
    if not l2:
        return l1

    # 针对 l1和l2的序列，进行逐项的合并，下面的过程就是一种递归的合并过程，  将L1和L2元素按照大小关系从小到大合并到一起的方法。
    if l1.val < l2.val:
        head = ListNode(l1.val)
        head.next = merge(l1.next, l2)
    else:
        head = ListNode(l2.val)
        head.next = merge(l1, l2.next)
    # 最后将 L1和L2合并的结果返回即可
    return head

