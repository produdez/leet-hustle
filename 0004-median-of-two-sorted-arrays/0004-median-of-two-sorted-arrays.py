class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
            Version: 1
            
            Idea:
            Binary search the left-portion of the median by:
            1. Getting the pivot of the first array (binary search)
            2. Prepare the left portion of median by getting the rest
                from the second array
            -> left por - first array pivot ... = second array pivot
            3. Validate result
                - Second array index must be valid (I)
                - left portion median split must be valid (II)
                -> first array's left <= second array's right
                -> and vice versa
            4. If split is valid
                -> Get result by
                if odd -> get mid max of the two right sides
                if even -> get average of left side's max 
                and right side's min
            Techniques:
            1. Swap the arrays so we always have longer array as nums1
            2. Add -inf and +inf at the two ends of the arrays
            to remove edge cases
            3. (I) invalid pivot 2
            - If piv2 < 0 -> move piv 1 to the left -> right = piv1 - 1
            - if piv2 is at last nums2 index -> reverse -> left = piv1 + 1
            
        '''
        if len(nums2) > len(nums1): nums1, nums2 = nums2, nums1

        for arr in [nums1,nums2]:
            arr.append(math.inf)
            arr.insert(0, -math.inf)
        
        left, right = 0, len(nums1) - 2
        left_portion_size = (len(nums1) + len(nums2)) // 2

        while left <= right:
            pivot1 = (left + right) // 2
            pivot2 = left_portion_size - (pivot1 + 1) - 1
            
            if pivot2 <= -1:
                # piv2 too small -> move piv1 left   
                right = pivot1 - 1
            elif pivot2 >= len(nums2) - 1:
                # piv2 too large -> move piv1 right           
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
                    return min(nums1[pivot1+1], nums2[pivot2+1]) 
                return (
                    max(nums1[pivot1], nums2[pivot2]) +
                    min(nums1[pivot1 + 1], nums2[pivot2 + 1])
                ) / 2
    
        
        