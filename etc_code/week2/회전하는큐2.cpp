#include <vector>
#include <deque>
#include <iostream>
#include <algorithm>

using namespace std;

void printQueue(deque<int> rotateQ) {
    for (auto i : rotateQ) {
        cout << i << " ";
    }
    cout << endl;
}

int findPosition(deque<int> &rotateQ, int num) {
    for (int i = 0; i != rotateQ.size(); ++i) {
        if (num == rotateQ[i]) return (i+1);
    }
    return 0;
}

int solution(int N, int M, vector<int> vv) {
    int answer = 0;
    int num = 0;
    int qSize = N;
    // cout << "N " << N << " M " << M << endl;
    deque<int> rotateQ(N);
    vector<int> pickQ(M);

    for (int i = 0; i < N; ++i) {
        rotateQ[i] = i + 1;
    }

    for (int i = 0; i < M; ++i) {
        pickQ[i] = vv[M - i - 1];
    }

    // for (int i = 0; i < pickQ.size(); ++i) {
    //     cout << pickQ.at(i) << " ";
    // }
    // cout << endl;
    

    while (pickQ.size() != 0) {
        num = pickQ.back();
        cout << num << " " << rotateQ.front() << endl;
        if (num == rotateQ.front()) {
            rotateQ.pop_front();
            pickQ.pop_back();
            --qSize;
        } else {
            int p = findPosition(rotateQ, num);
            // cout << "num position " << p << " r p " << rp << " qSize " << qSize << endl;
            printQueue(rotateQ);
            // if (p == 0) break;
            if (p > qSize/2 +1) {
                rotateQ.push_front(rotateQ.back());
                rotateQ.pop_back();
                ++answer;
            } else {
                rotateQ.push_back(rotateQ.front());
                rotateQ.pop_front();
                ++answer;
            }
        }
    }

    return answer;
}

int main(int argc, char** argv) {
    // cout << "answer " << solution(10, 3, {1,2,3}) << " == 0" << endl;
    cout << "answer " << solution(10, 3, {2,9,5}) << " == 8" << endl;
    // cout << "answer " << solution(32, 6, {27, 16, 30, 11, 6, 23}) << " == 59" << endl;
    // cout << "answer " << solution(10, 10, {1, 6, 3, 2, 7, 9, 8, 4, 10, 5}) << " == 14" << endl;
}