#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    sort(numbers.begin(), numbers.end());
    vector<int>::iterator iter;
    iter = numbers.begin();

    for (int i = 0; i < 10; ++i) {
        if (i != *iter) {
            answer += i;
        } else {
            ++iter;
        }
    }

    cout << answer << endl;
    return answer;
}


int main() {
    solution({1,2,3,4,6,7,8,0});
    solution({5,8,4,0,6,7,9});
}