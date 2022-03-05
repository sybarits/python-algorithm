#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    int d_size = dungeons.size();
    vector<int> v;
    for (size_t i = 0; i < d_size; i++) {
        v.push_back(i);
    }

    do {
        int tired = k;
        int temp = 0;
        for (int i = 0; i < d_size; i++) {
            if (tired >= dungeons[v[i]][0]) {
                tired -= dungeons[v[i]][1];
                temp++;
            } else {
                break;
            }
        }
        if (answer < temp) {
            answer = temp;
        }
        if (answer == d_size) {
            break;
        }
    } while (next_permutation(v.begin(), v.end()));

    return answer;
}


int main() {
    cout << solution(80, { {80,20},{50,40},{30,10} }) << endl;
}