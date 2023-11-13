#include <iostream>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.length() == 1)
            return s;

        string subString = s.substr(0, 1);
        for (int i=0; i<s.length(); i++) {
            int start=0, end=0;
            if (i < s.length()-1 && s[i] == s[i+1]) {
                start = i;
                end = i+1;

                while (true) {
                    if (start < 0 || end >= s.length())
                        break;
                    if (s[start] != s[end])
                        break;
                    else if ((end - start + 1) > subString.length()) {
                        subString = s.substr(start, end-start+1); 
                    }
                    start--;
                    end++;
                }
            }
            if (i > 0 && i < s.length()-1 && s[i-1] == s[i+1]) {
                start = i-1;
                end = i+1;

                while (true) {
                    if (start < 0 || end >= s.length())
                        break;
                    if (s[start] != s[end])
                        break;
                    else if ((end - start + 1) > subString.length()) {
                        subString = s.substr(start, end-start+1); 
                    }
                    start--;
                    end++;
                }
            }
        }
        return subString;
    }
};


int main() {
    Solution s;
    cout << s.longestPalindrome("ccc");
    return 0;
}