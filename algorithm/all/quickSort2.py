


def quickSort(array):
    if len(array) < 2 :
        return array
    low=0
    high=len(array)-1
    # 以第一个元素的值作为基准值
    tmp = array[low]
    while (low < high):
        # 将小于基准值的放到坐标，大于基准值的放到右边
        # 因为我们选定的基准值在最左边，所以我们要从右边的元素开始比较
        while (low < high and array[high] >= tmp):
            # 当比较元素的值大于基准值，继续移动指针
            high = high -1
        # 将指针high的值赋予元素low（此时hiah上的值应该是tmp，做一个位置的交换，但是tmp的位置还会继续改变）
        array[low] = array[high]
        # 此时low位置上的元素值一定小于基准值tmp
        while (low < high and array[low] <= tmp):
            # 当比较元素的值小于基准值，继续移动指针
            low = low + 1

        # 将指针low的值赋予元素high（）
        array[high] = array[low]
        # 此时确定tmp应该在的位置是low
        array[low] = tmp

    return quickSort(array[:(low)])+[array[low]]+quickSort(array[low+1:])


if __name__ == '__main__':
    print(quickSort([4, 5, 2, 1, 5, 6, 7, 8, 9, 6]))
    #  arr =[4, 5, 2, 1, 5, 6, 7, 8, 9, 6]
    #  print(arr[:3])
















