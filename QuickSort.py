"""
对于一个序列，先选第一个元素，找出其应该在的位置；
    找其位置的同时将比较过的元素简单排序，即：小于它的放左边，大于的放右边

再将该简单有序的lists分为2部分，对左右两个子序列递归排序。

"""
def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left-1)
    quick_sort(lists, left+1, high)
    return lists


a = quick_sort([50, 10, 90, 30, 70, 40, 80, 60, 20], 0, 8)
print(a)
