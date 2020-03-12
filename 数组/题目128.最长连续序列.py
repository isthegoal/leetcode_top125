# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精


'''
     题目：
        给定一个未排序的整数数组，找出最长连续序列的长度。
        要求算法的时间复杂度为 O(n)。

        示例:
            输入: [100, 4, 200, 1, 3, 2]
            输出: 4
            解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

        解释：这里的连续序列，是指 数值按照1递增的吧。



     分析：

     解法：

        题目要求 O(n) 复杂度。

        1.用哈希表存储每个端点值对应连续区间的长度
        2.若数已在哈希表中：跳过不做处理
        3.若是新数加入：
         (1)取出其左右相邻数已有的连续区间长度 left 和 right
         (2)计算当前数的区间长度为：cur_length = left + right + 1
         (3)根据 cur_length 更新最大长度 max_length 的值
         (4)更新区间两端点的长度值    【这里有个思考，更新了位置，分别是 当前位置，和连续的左边界、连续的右边界的位置，那中间的位置呢？明白了，中间的位置就没有用了，因为别人不会看它了，只会看边界两个锚点做连接即可。】
'''


class Solution(object):
    def longestConsecutive(self, nums):
        # 1.用哈希表存储 {每个端点值对应连续区间的长度}
        hash_dict = dict()
        max_length = 0


        for num in nums:
            # 2.若数已在哈希表中：跳过不做处理
            if num not in hash_dict:
                # (1)取出其左右相邻数已有的连续区间长度 left 和 right  （如果没有的话，就默认0）
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)

                #(2)计算当前数的区间长度为：cur_length = left + right + 1
                cur_length = 1 + left + right

                #(3)根据 cur_length 更新最大长度 max_length 的值  （最大值统计，可能有多个不错的连续长度的比较。）
                if cur_length > max_length:
                    max_length = cur_length

                #(4)更新区间两端点的长度值           多个位置上更新  表示 在当前端点下 所连接的  连续区间长度。 （其实慢慢的，就这三个位置设定就好，形成了连贯）
                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length

        # 最后获得 统计收集的最大值。
        return max_length