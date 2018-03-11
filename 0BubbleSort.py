"""
冒泡：
    原始版本：将i由0开始，与后面每一个j=i+1 进行比较，交换
                再i=1 ...这样好不容易换到前面第一位的容易被序列最后一个最小值直接怼到末尾去

    现在的更新版：i由0开始
                  j = length-2 与 j = length-1 进行比较，换位
                  确保移到上面的较小值不会有太大的变动 -- 见P381 图
"""


def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i, count-1)[::-1]:
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
    return lists
