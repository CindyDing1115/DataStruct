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
        while lists[right]>=key and left < right:
            right -= 1
        lists[left] = lists[right] # 这里必须先查找right，因为key = lists[left];若先查找左边，会覆盖最后一个right值
        
        while lists[left] <= key and left < right:
            left += 1
        lists[right] = lists[left] # 在这里覆盖正好还原了原始right位置应有的值
        
    lists[right] = key # 这里left == right 了
    quick_sort(lists,low,left-1)
    quick_sort(lists,left+1,high) # 这里的left已经找到了对应位置。
    
    return lists

a = quick_sort([50, 10, 90, 30, 70, 40, 80, 60, 20], 0, 8)
print(a)
