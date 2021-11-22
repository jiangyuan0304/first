# 它采用了一种分治的策略，通常称其为分治法
def QuickSort(ls):
    def partition(arr, left, right):
        key = left  # 划分参考数索引,默认为第一个数，可优化
        while left < right:
            while left < right and arr[right] >= arr[key]:
                right -= 1
            while left < right and arr[left] <= arr[key]:
                left += 1
            (arr[left], arr[right]) = (arr[right], arr[left])
        (arr[left], arr[key]) = (arr[key], arr[left])
        return left

    def quicksort(arr, left, right):  # 递归调用
        if left >= right:
            return
        mid = partition(arr, left, right)
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)

    # 主函数
    n = len(ls)
    if n <= 1:
        return ls
    quicksort(ls, 0, n - 1)
    return ls

# 1 3 5 2
x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = QuickSort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')