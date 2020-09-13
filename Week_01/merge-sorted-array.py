class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n:
            if m == 0:
                # nums1[n-1] = nums2[n-1]
                # n -= 1
                # continue
                # 根据评论者（梅行）建议改进
                nums1[:m+n] = nums2[:n]
                break
            if nums1[m-1] <= nums2[n-1]:
                nums1[m+n-1], nums2[n-1] = nums2[n-1], nums1[m+n-1]
                n -= 1
            else:
                nums1[m+n-1], nums1[m-1] = nums1[m-1], nums1[m+n-1]
                m -= 1