# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。
           将两数相加返回一个新的链表。除了数字 0 之外，这两个数字都不会以零开头。

           通俗点说就是 有两个链表分别表示两个数，我们需要获得 一个新的链表，链表的值表示两数相加的和。

                输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
                输出：7 -> 0 -> 8
                原因：342 + 465 = 807

      分析：
          类似于纸上计算两个数字的和，首先从最低有效位也就是列表L1 和 L2 的表头开始相加。
      由于每位数字都应当处于 0…9 的范围内，因此两个数字的和时可能会出现“溢出”。例如，5 + 7 = 12。
      在这种情况下，将当前位的数值设置为 22，并将进位 carry=1 带入下一次迭代。进位 carry 必定是 0 或 1，
      这是因为两个数字相加（考虑到进位）可能出现的最大和为 9 + 9 + 1 = 19。

      思路：
         先判断一下哪个链表长，然后用交换的方法确保一定是l1更长。
         然后把l2的值加到l1上，全部加完之后遍历l1处理进位，记得处理最后一位需要进1的特殊情况。【控制进位并相加到 到L1链表上】


        链表两数相加：carry存储进位，digit存储当前位值，
            res = (l1->val+l2->val+carry)%10，carry = (l1->val+l2->val+carry)/10；
            ListNode* tmpnode=new ListNode(res);
            PS：在两链表遍历完之后需要判断一下carry（即是否有最高位进位）
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        length1, length2 = 0, 0
        p = l1
        while p:
            length1 += 1
            p = p.next
        p = l2
        while p:
            length2 += 1
            p = p.next
        if length1 < length2:
            l1, l2 = l2, l1

        p1, p2 = l1, l2
        c = 0
        while p2:
            p1.val += p2.val
            p1 = p1.next
            p2 = p2.next
        p1 = l1
        while p1:
            p1.val += c
            c = 0
            if p1.val > 9:
                p1.val -= 10
                c = 1
            if not p1.next and c:
                p1.next = ListNode(1)
                break
            p1 = p1.next
        return l1
#___________________________________    练习1   ______________________________#
'''

    思路：
        就像你在纸上计算两个数字的和那样，我们首先从最低有效位也就是列表 l1 和 l2 的表头开始相加。
        由于每位数字都应当处于 0…9 的范围内，我们计算两个数字的和时可能会出现 “溢出”。
        例如，5+7=12。在这种情况下，我们会将当前位的数值设置为 2，并将进位 carry=1 
        带入下一次迭代。进位 carry 必定是 0 或 1，这是因为两个数字相加（考虑到进位）可能出现的最大和为 9+9+1=19。
        
        所以思路是比较简单的：就是使用链表的方式，模拟纸上的加法推算过程，并且低位在前、高位在后，是非常有力于推算的。
        
    伪代码如下：（非常好理解）

        1.将当前结点初始化为返回列表的哑结点。
        2.将进位 carry初始化为 0。
        3.将 p 和 q 分别初始化为列表 l1 和 l2 的头部。
        4.遍历列表 l1 和 l2 直至到达它们的尾端。
            （1）将 x 设为结点 p 的值。如果 p 已经到达 l1 的末尾，则将其值设置为 0。
            （2）将 y 设为结点 q 的值。如果 q 已经到达 l2 的末尾，则将其值设置为 0。
            （3）设定 sum=x+y+carry。
            （4）更新进位的值，carry=sum/10。
            （5）创建一个数值为 (sum mod 10) 的新结点，并将其设置为当前结点的下一个结点，然后将当前结点前进到下一个结点。
            （6）同时，将 p 和 q 前进到下一个结点。
        5.检查 carry = 1 是否成立，如果成立，则向返回列表追加一个含有数字 11 的新结点。
        6.返回哑结点的下一个结点


'''
class Solution1:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #  1  和  2两步，进行初始化信息  ，进位定义，创建用于存和的链表L3
        re = ListNode(0)
        r=re
        carry=0

        # 开始  进位计算。
        while(l1 or l2):
            #  对应 4的  （1）和（2）
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            # 对应 4的  （3），使用到进位进行相加计算。
            s=carry+x+y
            # 对应 4的  （4），获取得到和的进位值。
            carry=s//10
            # 对应 4的  （5），创建一个数值为 (sum mod 10) 的新结点，并更新指向
            r.next=ListNode(s%10)
            r=r.next
            # 对应 4的  （6），将 p 和 q 前进到下一个结点，进行下一个推位置
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        # 最后考虑进位剩余的情况。
        if(carry>0):
            r.next=ListNode(1)

        # re是预先留下的指针，其next就是通过r的走向创建的链表。
        return re.next
