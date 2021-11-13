# def SelectSort(ls):
#     n = len(ls)
#     if n <= 1:
#         return ls
#     for i in range(0, n - 1):
#         # 因为下标是从0开始的
#         minIndex = i
#         for j in range(i + 1, n):  # 比较一遍，记录索引不交换
#             if ls[j] < ls[minIndex]:
#                 minIndex = j
#             # 循环一遍找到那个最小的
#         if minIndex != i:  # 按索引交换
#             # 判断是否还是原来的索引
#             ls[minIndex], ls[i] = ls[i], ls[minIndex]
#     return ls
#
#
# x = input("请输入待排序数列：\n")
# y = x.split()
# arr = []
# for i in y:
#     arr.append(int(i))
# arr = SelectSort(arr)
# # print(arr)
# print("数列按序排列如下：")
# for i in arr:
#     print(i, end=' ')


def order(ls):

    if len(ls) <= 1:
        return ls

    for i in range(len(ls)-1):
        minindex = i
        for k in range(i+1, len(ls)):
            if ls[k] < ls[i]:
                minindex = k

        if minindex != i:
            ls[i], ls[minindex] = ls[minindex], ls[i]

    print(ls)

if __name__ == '__main__':
    order([1,4,5,2,8,5,4])







