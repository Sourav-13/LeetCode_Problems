class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        leftPivot = []
        rightPivot = []
        countPivot = nums.count(pivot)

        for num in nums:
            if num != pivot:
                if num < pivot:
                    leftPivot.append(num)
                else:
                    rightPivot.append(num)
        # leftPivot.extend([pivot] * countPivot + rightPivot)
        # return leftPivot
        return leftPivot + [pivot] * countPivot + rightPivot

