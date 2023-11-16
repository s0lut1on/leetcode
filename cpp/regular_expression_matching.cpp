#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        bool res = true;
        int indexS, indexP=0;
        for (indexS=0; indexS < s.size(); indexS++) {
            if (indexS >= p.size()) {
                res = false;
                break;
            }
            cout << "compare: " << indexS << "\t" << indexP << "\t" << s[indexS] << "\t" << p[indexP] << endl;
            if (s[indexS] == p[indexP]) {
                indexP++;
                continue;
            } else if (p[indexP] == '.') {
                indexP++;
                continue;
            } else if (p[indexP] == '*') {
                if (indexP+1 < p.size() && s[indexS] == p[indexP+1]) {
                    indexP += 2;
                    continue;
                } else if (s[indexS] == p[indexP - 1] || (indexP-1 >= 0 && p[indexP-1] == '.')) {
                    indexP++;
                    continue;
                } else {
                    res = false;
                    break;
                }
            } else if (indexP + 1 < p.size() && p[indexP+1] == '*') {
                indexP += 2;
                indexS--;
                continue;
            } else {
                res = false;
                break;
            }
        }
        if (indexP < p.size() && p[p.size()-1] != '*') {
            res = false;
        }
        return res;
    }
};

int main() {
    Solution s;
    cout << true << endl;
    cout << s.isMatch("aaa", "a*a") << endl;
    return 0;
}