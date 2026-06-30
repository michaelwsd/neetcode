class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic increasing stack 
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                idx, tmp = stack.pop()
                res[idx] = i - idx

            stack.append((i, temperatures[i]))

        return res