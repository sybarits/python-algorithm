#include <string>
#include <vector>
#include <deque>
#include <iostream>

using namespace std;

int getMaxP(deque<pair<int,int>> dq) {
    int result = 0;
    for (auto p : dq) {
        if (p.first > result) {
            result = p.first;
        }
    }
    return result;
}

int solution(vector<int> priorities, int location) {
    int answer = 0;
    deque<pair<int,int>> dq;

    int idx = 0;
    for (auto p: priorities) {
        dq.push_back(pair<int,int>(p,idx));
        ++idx;
    }

    int step = 1;
    int maxP = getMaxP(dq);
    while (true) {
        auto docu = dq.front();
        if (docu.first < maxP) {
            dq.pop_front();
            dq.push_back(docu);
        } else {
            if (docu.second == location) {
                return step;
            }
            dq.pop_front();
            maxP = getMaxP(dq);
            ++step;
        }
    }
    return answer;
}


int main() {

    cout << solution({2, 1, 3, 2},2) << endl;
    cout << solution({1, 1, 9, 1, 1, 1},0) << endl;
}