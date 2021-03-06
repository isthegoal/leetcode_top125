# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

            如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
            必须原地修改，只允许使用额外常数空间。
            以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
            1,2,3 → 1,3,2
            3,2,1 → 1,2,3
            1,1,5 → 1,5,1
      分析：


      思路：
         从右边找到第一对两个连续的数字 a[i]和 a[i−1]，它们满足 a[i]>a[i-1]。现在，没有对 a[i−1] 右侧的重新排列可以
         创建更大的排列，因为该子数组由数字按降序组成。因此，我们需要重新排列 a[i−1] 右边的数字，包括它自己。

         现在，什么样子的重新排列将产生下一个更大的数字呢？我们想要创建比当前更大的排列。因此，我们需要将数字 a[i−1] 替换为位于其右侧区域的
         数字中比它更大的数字，例如 a[j]。

         我们交换数字a[i−1] 和 a[j]。我们现在在索引 i−1 处有正确的数字。 但目前的排列仍然不是我们正在寻找的排列。
         我们需要通过仅使用 a[i−1]右边的数字来形成最小的排列。 因此，我们需要放置那些按升序排列的数字，以获得最小的排列。
         但是，请记住，在从右侧扫描数字时，我们只是继续递减索引直到我们找到 a[i] 和 a[i−1] 这对数。
         其中，a[i] > a[i-1]。因此，a[i−1] 右边的所有数字都已按降序排序。此外，交换 a[i−1] 和 a[j] 并未改变该顺序。
         因此，我们只需要反转 a[i−1] 之后的数字，以获得下一个最小的字典排列。

         https://blog.csdn.net/a_learning_boy/article/details/85239072


         对了，可以借鉴这里的思路，非常简单https://www.youtube.com/watch?v=w58KFpW5Pjk。很直白的，一次点破的讲述。
         （1）首先是 从后往前找到第一个  产生降序的数字，然后将这个数字位替换成其  后面中稍微比其大一个的数字。
         （2）然后对于后面剩余的位数进行排序即可。    这样的操作就能够实现获取得到在数字排序角度找到稍微更大一点的数字。【排序的原因是因为后面原来是升的321，现在改成降的123，这样子】

         想想还是很有道理的，在尽量往后的地方找到一个可替换的小数。
'''


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #  对应于第一步，找到这个由后向前产生  降序的数字位
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        # 针对这个数字位， 找到一个稍微比其大一点的数字。   也就是之前了解的升序中，第一个比其大的数字。  进行数字替换
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)

        #最后也就是对应于第二步，对剩下的数字进行 排序即可，因为  之前由后向前是升序的，所以只需要进行序列的逆置即可。
        self.reverse(nums, i + 1)

    # 序列逆置操作
    def reverse(self, nums, start):
        i = start
        j = len(nums) - 1
        #不断进行交换
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
#___________________________________    练习1   ______________________________#
#nums  可以是【1,2,3】这样的              【1,2,3,5,2,5,6,7,3,4】 下一个排序是 [1,2,3,5,2,5,6,7,4,3]
def fun1(nums):
    '''
    （1）首先是 从后往前找到第一个  产生降序的数字，然后将这个数字位替换成其  后面中稍微比其大一个的数字。
    （2）然后对于后面剩余的位数进行排序即可。    这样的操作就能够实现获取得到在数字排序角度找到稍微更大一点的数字。【排序的原因是因为后面原来是升的321，现在改成降的123，这样子】
             就是这两步，可以很稳的实现想要的效果
    '''
    #获取下一个更大点的排序
    i=len(nums)-2

    #从后往前 找到第一个产生降序的位置
    while i>=0 and nums[i+1]<=nums[i]:
        i-=1

    #找到后方 第一个产生 大于i位置的j。  如果找到了进行交换就是我们需要的更大一点的
    if i>=0:
        j=len(nums)-1
        while j>=0 and nums[j]<=nums[i]:
            j-=1
        swap(nums,i,j)

    #找到之后，对于后面的进行逆置， python下直接::不就行了....         这个逆置的作用是什么呢？？？
    return reverse(nums,i+1)

# 辅助函数- 交换
def swap(nums,i,j):
    nums[i],nums[j]=nums[j],nums[i]
# 辅助函数- 逆置   中折逆置方式
def reverse(nums,start):
    i=start
    j=len(nums)-1
    while i<j:
        swap(nums,i,j)
        i+=1
        j-=1


