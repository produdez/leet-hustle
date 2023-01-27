class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) > len(nums1): nums1, nums2 = nums2, nums1
        if len(nums1) == 1 and not nums2: return nums1[0]
        for arr in [nums1,nums2]:
            arr.append(math.inf)
            arr.insert(0, -math.inf)

        print(nums1, nums2)
        
        left, right = 0, len(nums1) - 2
        left_portion_size = (len(nums1) + len(nums2)) // 2
        while left <= right:
            pivot1 = (left + right) // 2
            
            pivot2 = left_portion_size - (pivot1 + 1) - 1
            # print(f'remain2 {remain2}, init p1: {pivot1}')
            # if remain2 < 0:
            #     # pivot1 += remain2
            #     # pivot2 = 0
            #     right = pivot1 - 1
            #     continue
            # elif remain2 >= len(nums2):
            #     # pivot1 += (remain2 - len(nums2)) + 1
            #     # pivot2 = len(nums2) - 2
            #     left = pivot1 + 1
            #     continue
            # # else:
            #     # pivot2 = remain2 - 1
            # pivot2 = remain2 - 1
            print(f'p1: {pivot1}, p2: {pivot2}')
            
            if pivot2 <= -1:
                right = pivot1 - 1
            elif pivot2 >= len(nums2) - 1:
                left = pivot1 + 1
            elif nums1[pivot1] > nums2[pivot2 + 1]: 
                # means nums1's pivot is too large
                right = pivot1 - 1
            elif nums2[pivot2] > nums1[pivot1 + 1]:
                # means nums2's pivot too small                 
                left = pivot1 + 1
            else:
                # means valid
                if (len(nums1) + len(nums2)) % 2 == 1:
                    print('odd')
                    # return max(nums1[pivot1], nums2[pivot2])
                    return min(nums1[pivot1+1], nums2[pivot2+1]) 
                # \
                #     if len(nums2) > 2 else nums1[pivot1]
                print('even')
                return (
                    max(nums1[pivot1], nums2[pivot2]) +
                    min(nums1[pivot1 + 1], nums2[pivot2 + 1])
                ) / 2
    
        
        