# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：
          给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，
          并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
          然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

            你需要计算完成所有任务所需要的最短时间。

            示例 1：

            输入: tasks = ["A","A","A","B","B","B"], n = 2
            输出: 8
            执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.


      分析
           题目得看两三遍才能看明白吧， 就是 A必须间隔n个时间 才能再走到A,所以这段间隔内，可以走B,或者待命什么也不敢。
                  然后问这样的特点下，给定一个任务序列，执行完的话，最短需要的时间是多少。


     思路



'''



'''
     主要参考解析：https://leetcode-cn.com/problems/task-scheduler/solution/python-xiang-jie-by-jalan/
     这个视频看两分钟就完全明白了。
      ________________
       理解的核心在于  对 计算式子  （k-1） * (n+1) +p  这个公式的理解。
       
       n+1是指每个 桶的大小，【桶的意思是指 A -> B -> (待命) -> A ->中 A -> B -> (待命)就是一个桶，一个A的间隔过程，其中A是出现最多的字母 】
       k-1是指 前k-1个桶都可以装满
       p是值最后的余下的，不用装满 时剩下的单独计算p个。
       
       为什么是n+1呢，是因为是以 A来看，A是出现最多的字母，A之后必须经过n个时间缓冲才能再A,所以A本身+n缓冲 =  1+n。
          而这里对于每个桶 n缓冲内的 可以放得东西是可以随意的，但是这n个间隔是必须的，才能把A放完。
          
       为什么是 k-1和p。  这也跟A的数量有关，已经决定了必须得有 (k-1)*(n+1)才能把A执行完，至于余下的 使用p时间执行即可。
       
       p表达的意思是 跟最大的出现次数单词A，比如出现3次，那么p就是出现3次字母的数量。    会伴随着A的出现，持续的出现，因此最后也会跟随着出现。
      ________________  
     有个疑问：加入  n非常小的情况下，比如n=1，那么A很快就能继续，比如  AAAAABBBCCCDD这样的。
                   走下来会是  A -> B->A ->B.....  因为n比较短，都不用停歇的。  感觉n必须比字母种类少，才能满足公式的形式。
     答：因为该问题，所以  （k-1） * (n+1) +p这个式子不是通用的， 还需要考虑的情况是 公式算出的值可能会比数组的长度小，
          如["A","A","B","B"]，n = 0，此时要取数组的长度，此时直接取 数组的长度即可，因为不会有 待命期。
    
        
       
        
     
     
     
     整体的解题步骤如下：
        1.计算每个任务出现的次数                                                                      为了找到出现次数最多的那个字母
        2.找出出现次数最多的任务，假设出现次数为 x                                                     为了计算出p，看有多少个一样次数的。
        3.计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time                                         代入一个通用的前部分
        4.计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count                           计算通用公式的后部分，得到p
        5.公式算出的值（k-1） * (n+1) +p可能会比数组的长度小,如果公式值比  数组的长度小，那么就  直接返回数组的长度 即可。
    
  



'''
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 边界条件
        length = len(tasks)
        if length <= 1:
            return length

        # 1.用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1

        # 2.按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]

        # 3.至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)

        # 4.计算出p
        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1

        # 5.如果结果比任务数量少，则返回总任务数,特殊情况的考虑
        return res if res >= length else length


