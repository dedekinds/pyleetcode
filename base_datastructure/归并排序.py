def merge(nums1,nums2):
    ans = []
    temp = len(nums1) + len(nums2)
    nums1.append(float('inf'))
    nums2.append(float('inf'))
    while len(ans) != temp:
        if nums1[0] <= nums2[0]:
            ans.append(nums1[0])
            nums1.pop(0)
        else:
            ans.append(nums2[0])
            nums2.pop(0)
    return ans


def mergesort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums)>>1
    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])
    return merge(left,right)