# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

            示例

            输入:
            [
              1->4->5,
              1->3->4,
              2->6
            ]
            输出: 1->1->2->3->4->4->5->6

      分析：


      思路：使用优先级队列，先存储每个链表首结点，优先级队列会自动对队列元素进行堆排序。
            将队列首结点.top()给phead下一个结点，然后把首节点的下一个结点入队（如果next不为nullptr），然后再建堆，直到队列为空

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        result = ListNode(-1)
        cur = result
        p = list()
        for i in lists:
            if i:
                heapq.heappush(p, (i.val, i))

        while len(p) > 0:
            cur.next = heapq.heappop(p)[1]
            cur = cur.next
            if cur.next:
                heapq.heappush(p, (cur.next.val, cur.next))

        return result.next

#___________________________________    练习1   ______________________________#
# 将多个有序的排序链表   合并在一起，  合并的结果也是有序的
# 非常简单的一种方式 是使用  最小堆的方法，首先将所有链表都压到堆中去，  之后再逐个从堆中  取出堆排序得到的结果，获得合并后的序列。
# heapq有两种方式创建堆, 一种是使用一个空列表,然后使用heapq.heappush()函数把值加入堆中,另外一种就是使用heap.heapify(list)转换列表成为堆结构
'''
使用堆这一数据结构，首先将每条链表的头节点进入堆中，然后将最小的弹出，并将最小的节点这条链表的下一个节点入堆，依次类推，
最终形成的链表就是归并好的链表。

heapq使用说明：

a为普通列表 
- heapq.heapify(a) 调整a，使得其满足最小堆 
- heapq.heappop(a) 从最小堆中弹出最小的元素 ，弹出仍然是一个最小堆
- heapq.heappush(a,b) 向最小堆中压入新的元素，压入仍然是一个最小堆

如果传进元组，第一个元素必须是要比较的值！


  时间复杂度为O(n*log(k))    空间复杂度为O(k)  
   这里的很舒服的，堆因为每次只放一个 链表的结点，所以使用k个空间大小就行。
'''
def mergeLists(lists):
    import heapq
    result=ListNode(-1)

    cur=result
    p=list()

    #对于链表列表，不断将  链表信息头结点  压入堆    p是载体  （注意是 链表头结点，利用这一头结点，我们可以用next往下找）
    for i in lists:
        if i:
            heapq.heappush(p,(i.val,i))

    #针对于 堆，不断进行最小值的排序
    while len(p)>0:
        # 不断进行链表的 附加，将堆中合适的放到 链表中
        cur.next=heapq.heappop(p)[1]
        cur=cur.next
        if cur.next:
            #因为之前只是头结点，所以这里 需要针对后面的信息，不断附加。
            heapq.heappush(p,(cur.next.val,cur.next))

    return result.next
