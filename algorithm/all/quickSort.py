
# 来自《算法图解》的快速排序写法 ，利用的是递归的技巧 分而治之的思想。

def quickSort(array):
    if len(array) < 2:
        # 基线条件：为空或者只包含一个元素的数组是“有序”的
        return array
    else:
        # 取第一个元素为基准值
        pivot = array[0]
        # 由所有小于等于基准值的元素组成的子数组
        # [i for i in arr[n:] ]  这个用法是从第n位开始遍历数组arr生产新的数组
        less = [i for i in array[1:] if i <=pivot]
        # 由所有大于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)

if __name__ == '__main__':
    print(quickSort([4, 5, 2, 1, 5, 6, 7, 8, 9, 4, 6, 3, 2]))
