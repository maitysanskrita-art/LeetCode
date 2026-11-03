class Solution:
    def originalDigits(self, s: str) -> str:
        c = [s.count(x) for x in "zwuxghfsoi"]

        nums = [0] * 10
        nums[0] = c[0]
        nums[2] = c[1]
        nums[4] = c[2]
        nums[6] = c[3]
        nums[8] = c[4]
        nums[3] = c[5] - nums[8]
        nums[5] = c[6] - nums[4]
        nums[7] = c[7] - nums[6]
        nums[1] = c[8] - nums[0] - nums[2] - nums[4]
        nums[9] = c[9] - nums[5] - nums[6] - nums[8]

        return ''.join(str(i) * nums[i] for i in range(10))