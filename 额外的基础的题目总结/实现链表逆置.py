# coding: utf-8
'''
    这里其实有三种解法
       【1】使用 外部空间方式的方法
       【2】不适用外部空间的 递归方法
       【3】不适用外部空间的 插入法

    接下来会主要介绍后两种
'''
##################################     对链表使用递归法进行逆序      ###################
#递归的方式，是首先递归  后面的小的部分，然后逐渐往前蔓延逆置过去。
def Reverse(head):
    if head is None:
        return
    #获取链表首结点， 并进行逆置
    firstNode=head.next
    newhead=RecuriveReverse(firstNode)
    head.next=newhead
    return newhead
'''
此处不明白偶，在 递归函数后的处理会对head造成影响吗？  我看直接返回的newhead，那你对head做的处理有什么用？
递归下是全局变量？？？
'''
def RecuriveReverse(head):
    #  使用 递归的方式，  不断对 单链表进行逆置。

    #最后到头的递归截止条件
    if head is None or head.next is None:
        return head
    else:
        #迭代的翻转，为了 首先对后面的 进行翻转吧
        newhead=RecuriveReverse(head.next)
        # 执行翻转的操作，这个可以看做两部分的颠倒吧
        head.next.next=head #这会对head本身造成影响吗？
        head.next=None #看到吗，现在原来的head.next已经放前面了，head原来所指部分放后面了
    return newhead#最后一步，把最后翻转的结果作为安徽即可吧