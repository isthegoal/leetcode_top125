# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

            示例 1 :
            输入:nums = [1,1,1], k = 2
            输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

      分析：

      思路：问连续子数组的题，首先考虑用前缀和数组解决。
            找到前缀和数组之后，这道题就变成了求前缀和数组里，两数之差为k的组合个数

          这里主要也是使用的前缀法，但是这里要明白  使用的字典是 defaultdict，而不是dict.

          其中两个字典方式的区别是：
             defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值（返回工厂函数的默认值，比如list返回的是[]）。
             而dict在没有存在字典中的key时，会产生报错。

'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        其实下面的解法  还挺绕脑的。
        """
        from collections import defaultdict
        pre_sum = 0
        record = defaultdict(int)
        record[0] = 1
        res = 0
        for i in range(len(nums)):
            print('pre_sum:',pre_sum)
            pre_sum += nums[i]
            res += record[pre_sum - k]

            print('pre_sum:', record[pre_sum])
            record[pre_sum] += 1
            print('pre_sum11:', record[pre_sum])

        return res

cla=Solution()
cla.subarraySum([1,2,1,4,5,3,6],5)

#___________________________________    练习1   ______________________________#
#  题意还是比较简单的，这里使用哈希表的解法吧。   这个有个重点，是可以要求不定长度的连续子序列。
'''
    借助哈希表保存累加和sum及出现的次数。若累加和sum-k在哈希表中存在，则说明存在连续序列使得和为k。
    则之前的累加和中，sum-k出现的次数即为有多少种子序列使得累加和为sum-k。
    
    1.初始化哈希表hash={0:1}，表示累加和为0，出现了1次。初始化累加和sum=0。初始化结果count=0
    2.遍历数组：
        -> 更新累加和sum+=nums[i]
        -> 若sum-k存在于hash中，说明存在连续序列使得和为k。则令count+=hash[sum-k]，表示sum-k出现几次，就存在几种子序列使得和为k。
        -> 若sum存在于hash中，将其出现次数加一。
        -> 若不存在，将其加入hash

    3.返回count
    
'''
def fun1(nums,k):
    # 初始化hash,hash 的形式是{累加和sum:出现的次数}
    hash={0:1}

    # sum是现有的累加和。   count是统计次数
    sum=0
    count=0

    #从前往后看hash
    for i in range(len(nums)):
        # 更新累加和sum+=nums[i]
        sum+=nums[i]
        # 如果  sum-k存在于hash中，说明存在连续序列使得和为k
        if ((sum-k) in hash):
            count+=hash[sum-k]
        # 如果 现在统计的累加和在  哈希的键中，则令值 +1即可
        if (sum in hash):
            hash[sum]+=1
        # 最后若不存在，将其加入hash
        else:
            hash[sum]=1

    return count

