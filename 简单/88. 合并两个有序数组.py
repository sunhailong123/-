from typing import List


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         if n == 0: return
#         j = 0
#         for i in range(m, len(nums1)):
#             nums1[i] = nums2[j]
#             j+=1
#         nums1.sort()
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         nums1[m:] = nums2
#         nums1.sort()
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sored = []
        p1,p2 = 0,0
        while p1<m or p2 <n:
            if p1 == m:
                sored.append(nums2[p2])
                p2+=1
            elif p2 == n:
                sored.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sored.append(nums1[p1])
                p1 += 1
            else:
                sored.append(nums2[p2])
                p2 += 1
        nums1[:] = sored

Solution().merge([1,2,3,0,0,0],3,[2,5,6],3)
