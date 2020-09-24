#冒泡排序
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
#选择排序
def selectionSort(a):
    n = len(a)

    for i in range(n-1):
        minindex = i
        for j in range(i+1,n):
            if a[j] < a[minindex]:
                a[j],a[minindex] = a[minindex],a[j]
    
    return a
#插入排序
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
    n = len(a)
    for i in range(n):
        preindex = i-1
        current = d[i]
        while preindex >=0 and current < d[preindex]:
            d[preindex+1] = d[preindex]
            preindex -= 1
        d[preindex+1] = current
    return d
#希尔排序 不稳定  平均：nlogn 最好：n（longn的平方）
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
a = [3,15,2,4,19,37,36,40,49,37]
# print(bottlSorted(a))
# print(selectionSort(a))
# print(insertionSort(a))
print(mergesort(a))