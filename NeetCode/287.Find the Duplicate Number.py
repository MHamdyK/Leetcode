class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashMap = set()
        for num in nums:
            if num in hashMap:
                return num
            else:
                hashMap.add(num)
