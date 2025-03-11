class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = 0,0
        while True:
            slow = nums[slow] # one hop
            fast = nums[nums[fast]] # two hops

            if slow == fast:
                break
        slow2 = 0
        while True:
            if slow2 == slow:
                break
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow