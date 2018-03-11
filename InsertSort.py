"""
直接插入排序：
    （）（8,2,5,3,10）
    （8）（2,5,3,10）
    （2,8）(5,3,10)
        ......
一个数组的增长率恰好与另一个减少率相同
故只需一个数组
"""

def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


a = insert_sort([8, 2, 5, 3, 10])
print(a)
