def mergeSort(array):
    # 基线条件
    if len(array) <2 :
        return array
    else:
         # 分割条件   不加int的结果是double类型
        mid = int(len(array) / 2)
        left_arr = [i for i in array[:mid]]
        right_arr = [i for i in array[mid:]]
        # 通过递归继续分割，直到最小
        mergeSort(left_arr)
        mergeSort(right_arr)
        return merge(array,left_arr,right_arr)

def merge(array,left_arr,right_arr):
    #定义下标 i 是array的下标，l是left_arr的下标，r是right_arr的下标
    i=0;l=0;r=0;
    # 当 l 和 r 都没有到数组尾的时候
    while(l<len(left_arr) and r <len(right_arr)):
        # 对 left 和 right中的数组进行比较
        # 等到的较大值放入array
        if(left_arr[l]<right_arr[r]):
            array[i]=left_arr[l]
            i+=1
            l+=1
        else:
            array[i]=right_arr[r]
            i+=1
            r+=1
    # 当只剩下其中一个数组的指针没有到达尾部时候，将这个数组依次放入array因为这个数组本身已经被排序好
    while(r < len(right_arr)):
        array[i]=right_arr[r]
        i+=1
        r+=1
    while(l<len(left_arr)):
        array[i]=left_arr[l]
        i+=1
        l+=1

    return array





if __name__ == '__main__':
    # mergeSort([4,2,1,3,5,6,7,2])
    print(mergeSort([4,2,1,3,5,6,7,2]))




