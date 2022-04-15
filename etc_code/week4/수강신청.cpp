#include <vector>
#include <set>
#include <iostream>

using namespace std;

int main(int argc, char** argv) {
    /*
    input
    3 8
    20103324
    20133221
    20133221
    20093778
    20140101
    01234567
    20093778
    20103325

    out put
    20103324
    20133221
    20140101
    */
    ios::sync_with_stdio(false);
    int K,L;
    cin >> K >> L;
    vector<string> answer(L);
    vector<string> result;
    set<string> s;
    for (int i = 0; i < L; ++i) {
        string num;
        cin >> num;
        answer[i] = num;
    }

    for (int i = L-1; i != -1; --i) {
        if (s.find(answer[i]) == s.end()) {
            s.insert(answer[i]);
            result.push_back(answer[i]);
        }
    }

    int start = result.size() - 1;
    int end = start - K;
    for (int i = start; i != -1 && i != end ; --i) {
        cout << result[i] << "\n";
    }
    
}
