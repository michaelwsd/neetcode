class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)

        res = []
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr[:])

            for n in freq:
                if freq[n] <= 0:
                    continue
                curr.append(n)
                freq[n] -= 1
                dfs(curr)
                curr.pop()
                freq[n] += 1

        dfs([])
        return res