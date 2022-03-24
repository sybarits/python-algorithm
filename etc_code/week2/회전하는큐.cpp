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

int main(int argc, char** argv) {
    int answer = 0;
    int N,M,num,qSize;

    cin >> N >> M;
    deque<int> rotateQ(N);
    vector<int> pickQ;
    qSize = N;
    for (int i = 0; i < N; ++i) {
        rotateQ[i] = i + 1;
    }

    while (M--) {
        cin >> num;
        pickQ.push_back(num);
    }
    
    reverse(pickQ.begin(), pickQ.end());
    
    while (pickQ.size() != 0) {
        num = pickQ.back();
        if (num == rotateQ.front()) {
            rotateQ.pop_front();
            pickQ.pop_back();
            --qSize;
        } else {
            int p = findPosition(rotateQ, num);
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

    cout << answer << endl;;
    // return 0;
}