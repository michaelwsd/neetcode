class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;

        for (int i = 0; i < nums.size(); i++) {
            int n = nums[i];
            int comp = target - n;
            if (m.count(comp)) {
                return {m[comp], i};
            }
            m[n] = i;
        }

        return {-1, -1};
    }
};
