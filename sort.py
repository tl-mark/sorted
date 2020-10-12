#不稳定排序：（希尔，选择，堆，快速）排序
#冒泡排序  稳定  时间复杂度：平均n平方，最坏n平方，最好n
def bottlSorted(a):
    n = len(a)#列表长度

    for i in range(n-1):
        for j in range(i+1,n):
            if a[i] >  a[j]:
                a[i],a[j] = a[j],a[i]
    
    # while 1:
    #     state = 0  # 假设本次循环没有改变
    #     for i in range(len(a) - 1):
    #         if a[i] > a[i + 1]:
    #             a[i], a[i + 1] = a[i + 1], a[i]
    #             state = 1  # 有数值交换，那么状态值置1
    #     if not state:  # 如果没有数值交换，那么就跳出
    #         break
    return a
#选择排序 不稳定  平均:n平方；最坏：n平方；最好：n平方
def selectionSort(a):
    n = len(a)

    for i in range(n-1):
        minindex = i
        for j in range(i+1,n):
            if a[j] < a[minindex]:
                a[j],a[minindex] = a[minindex],a[j]
    
    return a
#插入排序  稳定  平均:n平方；最坏：n平方；最好：n
def insertionSort(d):
    # d1 = [d[0]]
    # for i in d[1:]:
    #     state = 1
    #     for j in range(len(d1) - 1, -1, -1):
    #         if i >= d1[j]:
    #             d1.insert(j + 1, i)  # 将元素插入数组
    #             state = 0
    #             break
    #     if state:
    #         d1.insert(0, i)
    # return d1
    n = len()
    for i in range(n):
        preindex = i-1
        current = d[i]
        while preindex >=0 and current < d[preindex]:
            d[preindex+1] = d[preindex]
            preindex -= 1
        d[preindex+1] = current
    return d
#希尔排序 不稳定  平均:n（1.3）；最坏：n平方；最好：n
def shellSort(arr):
    gap = 1
    n = len(arr)
    while gap < n//3:
        gap = gap*3+1
    while gap >0:
        for i in range(1,n):
            curnum,preindex = arr[i],i-gap
            while preindex >=0 and curnum < arr[preindex]:
               arr[preindex+gap] = arr[preindex]
               preindex -= gap
            arr[preindex+gap] = curnum
        gap //= 3
    return arr

#归并排序  nlogn 稳定
def mergesort(num):
    def merge(left,right):
        result = []
        i,j = 0,0
        while i <len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result+left[i:]+right[j:]
    if len(num) == 1:
        return num
    middle = len(num)//2
    left = mergesort(num[:middle])
    right = mergesort(num[middle:])
    return merge(left,right)
#快排 不稳定 平均nlogn
def quicksort(a):
    if len(a)<=1:
        return a
    pivot = a[0]
    left = [a[i] for i in range(1,len(a)) if a[i]<pivot]
    right = [a[i] for i in range(1,len(a)) if a[i] >= pivot]
    return quicksort(left)+[pivot]+quicksort(right)
def quickSort2(nums, left, right):  # 这种写法的平均空间复杂度为 O(logn)
    # 分区操作
    def partition(nums, left, right):
        pivot = nums[left]  # 基准值
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]  # 比基准小的交换到前面
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]  # 比基准大交换到后面
        nums[left] = pivot # 基准值的正确位置，也可以为 nums[right] = pivot
        return left  # 返回基准值的索引，也可以为 return right
    # 递归操作
    if left < right:
        pivotIndex = partition(nums, left, right)
        quickSort2(nums, left, pivotIndex - 1)  # 左序列
        quickSort2(nums, pivotIndex + 1, right) # 右序列
    return nums
#堆排序  不稳定  平均nlogn
# 大根堆（从小打大排列）
def heapSort(nums):
    # 调整堆
    def adjustHeap(nums,i,size):
        lchild = i*2+1
        rchild = i*2+2
        largest =i
        if lchild<size and nums[lchild] > nums[largest]:
            largest = lchild
        if rchild<size and nums[rchild] > nums[largest]:
            largest = rchild
        if largest !=i:
            nums[i],nums[largest] = nums[largest],nums[i]
            adjustHeap(nums,largest,size)
    def builtHeap(nums,size):
        for i in range(size//2)[::-1]:
            adjustHeap(nums,i,size)
    size = len(nums)
    builtHeap(nums,size)
    for i in range(size-1,-1,-1):
        nums[0],nums[i] = nums[i],nums[0]
        adjustHeap(nums,0,i)
    return nums
#计数排序 稳定 复杂度 n+m
def countingSort(nums):
    bucket = [0] * (max(nums) + 1) # 桶的个数
    for num in nums:  # 将元素值作为键值存储在桶中，记录其出现的次数
        bucket[num] += 1
    i = 0  # nums 的索引
    for j in range(len(bucket)):
        while bucket[j] > 0:
            nums[i] = j
            bucket[j] -= 1
            i += 1
    return nums
#桶排序 稳定 复杂度n+k
def bucketSort(nums, defaultBucketSize = 5):
    maxVal, minVal = max(nums), min(nums)
    bucketSize = defaultBucketSize  # 如果没有指定桶的大小，则默认为5
    bucketCount = (maxVal - minVal) // bucketSize + 1  # 数据分为 bucketCount 组
    buckets = []  # 二维桶
    for i in range(bucketCount):
        buckets.append([])
    # 利用函数映射将各个数据放入对应的桶中
    for num in nums:
        buckets[(num - minVal) // bucketSize].append(num)
    nums.clear()  # 清空 nums
    # 对每一个二维桶中的元素进行排序
    for bucket in buckets:
        insertionSort(bucket)  # 假设使用插入排序
        nums.extend(bucket)    # 将排序好的桶依次放入到 nums 中
    return nums
#基数排序  稳定 复杂度n*k
# LSD Radix Sort
def radixSort(nums):
    mod = 10
    div = 1
    mostBit = len(str(max(nums)))  # 最大数的位数决定了外循环多少次
    buckets = [[] for row in range(mod)] # 构造 mod 个空桶
    while mostBit:
        for num in nums:  # 将数据放入对应的桶中
            buckets[num // div % mod].append(num)
        i = 0  # nums 的索引
        for bucket in buckets:  # 将数据收集起来
            while bucket:
                nums[i] = bucket.pop(0) # 依次取出
                i += 1
        div *= 10
        mostBit -= 1
    return nums
a = [16,15,2,4,19,37]
# print(bottlSorted(a))
# print(selectionSort(a))
# print(insertionSort(a))
# print(mergesort(a))
# print(quickSort2(a,0,len(a)-1))
# print(bucketSort(a))
print(radixSort(a))