class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # ensure A is the smaller arr
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            mid_a = (l + r) // 2
            mid_b = half - mid_a - 2 # account for 0-indexing of B array and also from mid_a in the formula

            # out of bounds edge cases // set proper val
            Aleft = A[mid_a] if mid_a >= 0 else float("-inf") 
            Aright = A[mid_a + 1] if (mid_a + 1) < len(A) else float("inf")

            Bleft = B[mid_b] if mid_b >= 0 else float("-inf") 
            Bright = B[mid_b + 1] if (mid_b + 1) < len(B) else float("inf")

            # correct partition
            if Aleft <= Bright and Bleft <= Aright:

                # odd num of elements
                if total % 2:
                    return min(Aright, Bright)
                # even num of elements
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 

            # A left partition is too large
            elif Aleft > Bright:
                r = mid_a - 1
            else:
                l = mid_a + 1


