#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for ( auto i : scoville) {
        pq.push(i);
    }

    while (K > pq.top() && 1 != pq.size()) {
        int a = pq.top();
        pq.pop();
        int b = pq.top();
        pq.pop();
        pq.push(a+b*2);
        ++answer;
    }

    if (pq.size() == 1 && K > pq.top()) {
        return -1;
    }

    return answer;
}

int main() {
    cout << "answer " << solution({1, 2, 3, 9, 10, 12},7) << endl; 
}