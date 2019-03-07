def binsearch(nums,target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)>>1
        print(mid)
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1
