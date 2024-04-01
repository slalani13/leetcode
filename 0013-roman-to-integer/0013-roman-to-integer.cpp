using namespace std;
class Solution {
public:
    int romanToInt(string s) {
        map<char, int> mp;
        mp['I'] = 1;
        mp['V'] = 5;
        mp['X'] = 10;
        mp['L'] = 50;
        mp['C'] = 100;
        mp['D'] = 500;
        mp['M'] = 1000;
        string:: iterator it;
        it = s.end();
        int sum = *it;
        for (it = s.end()-1; it != s.begin()-1; it--) {
            if (mp[*it] < mp[*(it+1)]) {
                cout << "it:" << *it << endl;
                cout << "it+1:" << *(it+1) << endl;
                sum -= mp[*it];
                cout << "Map Value:" << mp[*it] << endl;
            }
            else {
                sum += mp[*it];
                cout << "Iterator:" << mp[*it] << endl;
            }
        }
        return sum;
    }
};