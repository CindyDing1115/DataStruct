
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    #这里拆分至num=1，此时left=[50]right=[10] merge之后 num=2对应的left=[10,50],此时right=[90,30]
    #再对right拆分->[30,90] 再merge ->[10,30,50,90]
    return merge(left, right)


a = merge_sort([50, 10, 90, 30, 70, 40, 80, 60, 20])
print(a)
