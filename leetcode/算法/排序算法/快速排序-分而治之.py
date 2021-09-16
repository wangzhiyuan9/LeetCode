def quick_sort(data):
    """快速排序"""
    if len(data)>=2:
        mid = data[len(data)//2]
        left,right = [],[]
        data.remove(mid)
        for i in data:
            if i >= mid:
                right.append(i)
            else:
                left.append(i)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


# 示例：
array = [2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
print(quick_sort(array))