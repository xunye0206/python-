def bubble_sort(li):
    # 遍历数组
    for i in range(len(li)):
        # 标记是否发生过交换位置
        sort = False
        # 在当前位置开始检查谁是最大的数，将其换到前面去
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j+1],li[j] = li[j],li[j+1]
                sort = True
        # 没有位置交换的话直接退出循环
        if not sort:
            break
            
    
array = [64, 34, 25, 12, 22, 11, 90]

print("排序前的数组:", array)

bubble_sort(array)

print("排序后的数组:", array)