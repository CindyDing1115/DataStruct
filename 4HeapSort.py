"""
将数组对应为完全二叉树
先构建大顶堆 -- 仅需根节点 > 子节点
交换data[0] 与 data[-1]位置
 向下调整，只选出子树中最大的与其根节点比较。
        根节点大 -- 不变
        根节点小 -- 下移
"""
def AdjustHeap(lists,i,idx):
    """
    :param lists: 序列
    :param i: 当前最后一个非叶子结点的序号
    :param idx: 当前最后一个未被排序的位置 -- 还有多少需要排序
    """
    temp = lists[i]
    j = 2 * i + 1
    while j <= idx:
        #python & 是位运算，and才是逻辑运算符
        if lists[j] < lists[j + 1] and j+1 <= idx: # j+1 < size 比如进行到最后两项，size下没有右结点，则必然小于已排好序的 like 30
            j += 1
        if temp > lists[j]:
            break
        lists[i] = lists[j]
        i = j
        j = j * 2 + 1
    lists[i] = temp


def HeapSort(lists):
    """
    1 整体排序  2 微调
    :param lists:
    :return:
    """
    length = len(lists)
    #这一步构建一个大顶堆，并找到了最大的元素放在[0]的位置
    #for i in range(0,(length-2)//2+1)[::-1]: #length-1 才是对应的元素索引，对其双亲结点要 (index-1）/2 故：length-2 // 2 而range不含最后一项 再+1
    for i in range(0, length // 2)[::-1]:
        AdjustHeap(lists, i, length-1)

    for i in range(length)[::-1]:
        lists[i], lists[0] = lists[0], lists[i] # 交换[0]与最后一个未被排序元素的位置
        AdjustHeap(lists, 0, i-1) #这时，最后一个位置算是有序了，未被排序的位置少了一个，故 -1

    return lists


a = HeapSort([50, 10, 90, 30, 70, 40, 80, 60, 20])
print(a)

