'''

    题目：在给定的网格中，每个单元格可以有以下三个值之一：

            值?0?代表空单元格；
            值?1?代表新鲜橘子；
            值?2?代表腐烂的橘子。
            每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

            返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回?-1。

                 输入：[[2,1,1],[1,1,0],[0,1,1]]
                 输出：4



'''

#  解法一。 非常直观的思路，但是时间跑的太长了
#   思路非常直接，  就是  进行标记 和传播，传播过程中进行修改和调整，并进行多波的传播，直到 没有橘子变坏为止。
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        bad_list = []
        good_list = []
        #   找到所有坏橘子的 坐标，并标记好橘子
        for l, item in enumerate(grid):
            # 对每个橘子，按照编号，进行附加
            for g, oringe in enumerate(item):
                # 这里是把  坏橘子的   坐标附加过去。
                if oringe == 2:
                    bad_list.append((l, g))
                elif oringe == 1:
                    good_list.append((l, g))

        # 设定边界。  分别是长度 和 宽度两个边界
        max_l = l
        max_g = g
        step = 0
        # 做的统计      我们现在开始进行多次传播，来看多少次能够把所有的好橘子都变坏完
        while good_list:

            #  对发生变化的信息做统计
            change_flag = False
            change_list = []

            # 传播吧.   首先收集所有能够发生 改变的假定位置
            for l, g in bad_list:
                if l - 1 >= 0:
                    change_list.append((l - 1, g))
                if l + 1 <= max_l:
                    change_list.append((l + 1, g))
                if g - 1 >= 0:
                    change_list.append((l, g - 1))
                if g + 1 <= max_g:
                    change_list.append((l, g + 1))
            # 根据 预假定的位置，进行正式传播更改的  设置
            for chang in change_list:
                if chang in good_list:
                    #  橘子变坏吧,  坐标设定
                    bad_list.append(chang)
                    good_list.remove(chang)
                    change_flag = True

            step += 1

            #   终止条件，不会传播时
            if not change_flag:
                break

        # 对于还有好的列表，说明传不完
        if good_list:
            return -1
        else:
            return step
