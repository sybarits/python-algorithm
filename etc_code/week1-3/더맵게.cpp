#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue< int, vector<int>, greater<int> > minHeap;
    for (int i = 0; i != scoville.size(); ++i) {
        minHeap.push(scoville[i]);
    }
    
    while (true) {
        int a = minHeap.top();
        if (a > K) break;
        minHeap.pop();
        if (minHeap.size() == 0) {
            return -1;
        }
        int b = minHeap.top();
        minHeap.pop();
        minHeap.push(a+b*2);
        ++answer;
    }

    cout << answer << endl;
    return answer;
}


int main() {
    solution({1, 2, 3, 9, 10, 12}, 7);
}