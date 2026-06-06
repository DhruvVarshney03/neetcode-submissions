class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # Always binary search the smaller array
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        half = (m + n + 1) // 2

        left, right = 0, m

        while True:
            i = (left + right) // 2   # partition in A
            j = half - i              # partition in B

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            # Correct partition found
            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2:
                    return float(max(Aleft, Bleft))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            # Need to move i left
            elif Aleft > Bright:
                right = i - 1
            # Need to move i right
            else:
                left = i + 1