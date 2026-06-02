class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        ptr1 = 0
        ptr2 = 0
        res = []

        while ptr1 < len(nums1) and ptr2 < len(nums2):

            if nums1[ptr1] == nums2[ptr2]:
                res.append(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1

            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1

            else:
                ptr1 += 1

        return res