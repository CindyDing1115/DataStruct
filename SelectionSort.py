"""
选择排序：
    将第一个作为极值与后面逐个比较，找到当前最小值放到相对最前。
"""
def select_sort(lists):
    count = len(lists)
    for i in range(0, count):
        minval = i
        for j in range(i+1, count):
            if lists[minval] > lists[j]:
                minval = j
        lists[minval], lists[i] = lists[i], lists[minval]
    return lists

