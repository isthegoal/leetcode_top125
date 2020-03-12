print('———————————      冒泡排序      —————————')
def bubblesort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]  #非常舒服的，不用中间变量的交换方式....


print('———————————      选择排序(每次选择最小的进行交换)      —————————')
def selectaort(arr):
    for i in range(len(arr)-1):
        #最小数的索引
        minindex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minindex]:
                minindex=j
        # i 如果不是最小数，则 进行i  和找到的最小数的交换
        if i!= minindex:
            arr[i],arr[minindex]=arr[minindex],arr[i]
    return arr

print('———————————      插入排序      —————————')
#在当前序列上进行的处理...
def insertionsort(arr):
    for i in range(len(arr)):
        preindex=i-1
        current=arr[i]
        #这里是腾出位置  往前挪...   比要比较大的都往后弄懂，然后我们就找到了合适的位置，插进去即可
        while preindex>=0 and arr[preindex]>current:
            arr[preindex+1]=arr[preindex]
            preindex-=1
        arr[preindex+1]=current
    return arr

print('———————————      希尔排序（递减增量排序  间隔由5 .. 3 ..1 由增量序列做间隔，趟内做直接插入排序）      —————————')
import math
def shellsort(arr):
    gap=1
    #这里是构造增量上的间隔值，  这里先计算初始gap，增量gap会在后面的计算过程中不断减小，不断的变成1。
    #下面是一种构造增量的方式吧，是灵活而可选的...
    while(gap<len(arr)/3):
        gap=gap*3+1

    while(gap>0):
        #下面的构成很好理解，就是在gap增量间隔下的  插入排序
        for i in range(gap,len(arr)):
            temp=arr[i]
            j=i-gap

            while j>=0 and arr[j]>temp:
                arr[j+gap]=arr[j]
                j-=gap
        gap=math.floor(gap/3)
    return arr


print('———————————      归并排序（两两组内进行排序，核心还是递归的思想）      —————————')
def mergesort(arr):

    if(len(arr)<2):
        return arr
    middle=math.floor(len(arr)/2)
    #是一种树形式的展开，由叶子节点不断不断的往上进行合并...... 越往上进行merge函数要合并的子集越大
    left,right=arr[0:middle],arr[middle:]
    return merge(mergesort(left),mergesort(right))

def merge(left,right):
    #这里看做简单的对两个  列表的合并即可。   会对两边的默认有序的集合(如果是第一次的话，因为就一个) 进行再排序合并
    result=[]
    while left and right:
        if left[0]<=right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result

print('———————————      快速排序（非常非常常用的排序方式）      —————————')
'''
在数列之中，选择一个元素作为”基准”（pivot），或者叫比较值。
数列中所有元素都和这个基准值进行比较，如果比基准值小就移到基准值的左边，如果比基准值大就移到基准值的右以基准值左右两边的子列作为新数列，不断重复第一步和第二步，直到所有子集只剩下一个元素为止。
举个例子，假设我现在有一个数列需要使用快排来排序：[11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22]，我们来看看使用快排的详细步骤：
选取中间的66作为基准值（基准值可以随便选）
数列从第一个元素11开始和基准值66进行比较，小于基准值，那么将它放入左边的分区中，第二个元素99比基准值66大，把它放入右边的分区中。
然后依次对左右两个分区进行再分区，直到最后只有一个元素分解完成再一层一层返回，返回规则是：左边分区+基准值+右边分区


感觉跟归并排序有一定相似把（一种分治的思想），只不过这里是不断设定基元 进行的排序（小于的放左边，大于的放右边，放的边上不保障有序）， 而归并排序是两两进行的合并。

emm....感觉跟归并好像好像....  但是这里是按大小值区分开分离的，而归并是直接按索引分离、然后做插入排序的...
有很多实现方式，但是每一步快排的思想都是一致的，就是针对一个基元 ，让小的位于其左边，大的位于其右边（分治子任务）。


快速排序的最坏运行情况是 O(n?)，比如说顺序数列的快排。但它的平摊期望时间是 O(nlogn)，且 O(nlogn) 
记号中隐含的常数因子很小，比复杂度稳定等于 O(nlogn) 的归并排序要小很多。所以，对绝大多数顺序性较弱的随机数列
而言，快速排序总是优于归并排序。
'''

def quick_sort(b):
    if len(b)<2:
        return b
    mid=b[len(b)/2]  #基元初始可以选择中间的，  这也更容易理解
    left ,right=[],[]  #存储比基元 大 和比基元小的元素

    b.remove(mid)

    for item in b:
        if item>mid:
            right.append(item)
        else:
            left.append(item)
    return quick_sort(left)+[mid]+quick_sort(right)


#####  第二种快排方式，比较常用的一种   **  高低位指针 **  （看下印象笔记中的解释，虽然有点小区别）
def partiton(li, low, high):  #这里是快排 最核心的函数部分，可以看到这里  的基元位置选取是直接选择的 当前区域的首个结点，要注意这样做的原因是左右两部分有明确的大小区分。
    key = li[low]
    while low < high:
        while low < high and li[high] >= key:
            high -= 1
        if low < high:
            li[low], li[high] = li[high], li[low]  #这里和印象笔记中的方式有点不一样，这里是交换的，印象笔记中是直接替换。

        while low < high and li[low] < key:
            low += 1
        if low < high:
            li[high], li[low] = li[low], li[high]
    #这个非常重要，是 按基准下大小分离的 标志。   小于low坐标的都比基准下，大于low的都比基准大。
    return low

def quickSort(li, low, high):
    if low >= high:
        return
    center = partiton(li, low, high)  #这里是个核心，我们每次是以   基元位置 为新的出发点 ， 进行分治在排序，对分离后的左右两部分分别进行   快排的通用过程
    #在基准分离后，再进行分治求解，很类似于  第一种方式的思想，只不过 这里之前的基准都是选择中间的，这里的基准位置是不固定的，但是都是n次
    quickSort(li, low, center - 1)
    quickSort(li, center + 1, high)


#一行代码实现的方式，也很牛逼
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
quick_sort(23,52,41)


#####  第四种快排方式，也是比较中规中矩自己喜欢的方法  ####
def kuaisu(arr):
    #考频最高的快速排序   程序还是挺复杂的。  但是道理很简单，每次找到一个数，然后比它小的在左边，比它大的在右边，这样合适的位置
    #以下使用高低位指针的方式
    n=len(arr)-1
    quicksort(arr,0,n)
    return arr
def quicksort(arr,low,high):
    if low<high: #进行多次这样的过程， 是一种由递归缩小范围的过程，  快速中也用到了递归，这个要注意下吧
        pi=partition(arr,low,high) #这个是快速的核心单步， 实现在pi位置之前的 都小于一个数，之后的都大于一个数

        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

def partition(arr,low,high):
    #开始核心的单步的定义过程。  这里是执行了在高低指针下，不断交换找到合适位置的过程
    key=arr[low]

    while low<high:
        #首先是 从后往前的看，遇到小的就交换
        while low<high and arr[high]>key:
            high-=1
        if low<high:
            arr[low],arr[high]=arr[high],arr[low]

        #接下来从前往后走吧
        while low<high and arr[low]<key:
            low+=1
        if low<high:
            arr[high],arr[low]=arr[low],arr[high]
    return low #最后low所处的位置就是中间  位置


print('———————————      堆排序（先创建堆，再不断取队顶https://www.jianshu.com/p/d174f1862601）      —————————')
'''
首先将待排序的数组构造出一个大根堆
取出这个大根堆的堆顶节点(最大值)，与堆的最下最右的元素进行交换，然后把剩下的元素再构造出一个大根堆
重复第二步，直到这个大根堆的长度为1，此时完成排序。
'''

from collections import deque
def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L

def heap_adjust(L, start, end):#感觉这函数写的不怎么对       进行调整，在初始构建堆和 后期取值都特别需要的步骤，从最大的非叶子节点开始比较并调整。
    #核心的，进行交换后，再次调整成大根堆的过程
    #这个函数其实就是把每个子树的根节点和较大的子节点进行值交换。而且如果在左子树 依然是根节点的情况下继续进行调整
    # 。 读者可以自己照着图调整几次就可以很好的理解代码的含义了。
    temp = L[start]
    i = start
    j = 2 * i #直接的孩子位置

    #此处就是找到其下的结点...  找到合适的进行替换的方式...但是感觉可能有一些错过...
    while j <= end:
        if (j < end) and (L[j] < L[j + 1]): #判断孩子的兄弟是否更为大
            j += 1
        if temp < L[j]: #如果右孩子大的话，直接针对右孩子做计算， 会不会错过左孩子下潜在大的值
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp #这个取出来的，放在最后位置的，进行交换的结点..

def heap_sort(L):
    #堆排序 主函数，   可以理解为两步走，先交换，再取元素，并进行堆的再次调整。
    L_length = len(L) - 1 #引入辅助空间

    first_sort_count = L_length / 2
    # 把序列调整为一个大根堆(heap_adjust函数)   不断调整，转成大根堆... 进行了4次的交换吧，对4个非叶子节点做的操作
    for i in range(first_sort_count):
        heap_adjust(L, first_sort_count - i, L_length)

    # 把堆顶元素和堆末尾的元素交换(swap_param函数)，然后把剩下的元素调整为一个大根堆。 这里应该算是核心.....用最后一个做交换再进行再次的调整。
    for i in range(L_length - 1):
        L = swap_param(L, 1, L_length - i)
        #可以明显看出，这里是全调整，跟上一个调整有很大的区别，这里会从开头到最后都进行查找交换
        heap_adjust(L, 1, L_length - i - 1)
    return [L[i] for i in range(1, len(L))]

def heap_sort_main():
    #使用python库中提供的链表结构   三步走吧，这里是构建堆的过程，使用一个链表表示... 第二步是调整形成大根堆... 第三步是对大根堆进行取堆顶并调整
    #python 的list 可以用insert在最左边插入0呀   不过list的insert操作时间复杂度是O(n) deque是O(1)
    L = deque([50, 16, 30, 10, 60,  90,  2, 80, 70])
    L.appendleft(0)
    print(heap_sort(L))

print('———————————      基数排序（按位排序，从低位往高位排...以下是非常精简有效的方式）      —————————')
def radix_sort(list):
    i=0
    #获取最大的、可能使用到的位数j
    max_num=max(list)
    d=len(str(max_num))

    for k in range(d):
        s=[[] for i in range(10)] #桶的概念  构建出10个桶，每个桶都是一个列表，分别表示不同的位数
        for i in list:
            '''对于3个元素的数组[977, 87, 960]，第一轮排序首先按照个位数字相同的
                           放在一个桶s[7]=[977],s[7]=[977,87],s[0]=[960]
                           执行后list=[960,977,87].第二轮按照十位数，s[6]=[960],s[7]=[977]
                           s[8]=[87],执行后list=[960,977,87].第三轮按照百位，s[9]=[960]
                           s[9]=[960,977],s[0]=87,执行后list=[87,960,977],结束。'''
            s[i/(10**k)%10].append(i) #977/10=97(小数舍去),87/100=0   进行数的桶归属计算
        list=[j for i in s for j in i] #这个非常关键，这样百分位排序时会使用到十分位计算得到的序列....
    return list

if __name__=='__main__':
    a=[977, 87, 960]
    radix_sort(a)
    print(a)










