#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        if (nums.size() == 0)
            return "";
        int lengthNum = nums[0].size();
        string res(lengthNum, '0');
        int index = 0;
        while (find(nums.begin(), nums.end(), res) != nums.end()) {
            res.replace(index, 1, "1");
            index++;  
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<string> nums = {"00", "01"};
    cout << s.findDifferentBinaryString(nums);
    return 0;
}