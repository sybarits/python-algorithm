#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <stack>
#include <iostream>

using namespace std;

int validBracket(vector<char> &vchar, map<char, char> &bmap) {
    if (vchar.size() == 0) {
        return 0;
    }
    stack<char> cstack;
    for (size_t i = 0; i < vchar.size(); i++)
    {
        if (cstack.empty() || bmap.count(vchar[i]) == 0) {
            cstack.push(vchar[i]);
        } else if (!cstack.empty() && cstack.top() == bmap[vchar[i]]) {
            cstack.pop();
        }
    }
    if (cstack.empty()) {
        return 1;
    }
    return 0;
}

int solution(string s) {
    int answer = 0;
    const int ssize = s.length();
    vector<char> vchar(s.begin(), s.end());
    map<char, char> bmap;
    bmap.insert(pair<char,char>(')','('));
    bmap.insert(pair<char,char>('}','{'));
    bmap.insert(pair<char,char>(']','['));

    for (size_t i = 0; i < ssize; i++)
    {
        cout << vchar[i] << endl;
        cout << validBracket(vchar, bmap) << endl;
        answer += validBracket(vchar, bmap);
        char temp = vchar[ssize-1];
        vchar.pop_back();
        vchar.insert(vchar.begin(), temp);
    }
    

    return answer;
}


int main() {
    
    // map<char, char> bmap;
    // bmap.insert(pair<char,char>(')','('));
    // bmap.insert(pair<char,char>('}','{'));
    // bmap.insert(pair<char,char>(']','['));
    // cout << bmap[')'] << endl;

    cout << solution("[](){}") << endl;


}