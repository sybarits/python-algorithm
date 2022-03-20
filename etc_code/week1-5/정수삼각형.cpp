#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    vector<vector<int>> sum;
  
    sum.assign(triangle.begin(), triangle.end());
  
    for (int i = 0; i < triangle.size()-1; ++i) {
        for (int j = 0; j < triangle[i].size(); ++j) {
            if (sum[i+1][j] < sum[i][j] + triangle[i+1][j]) {
                sum[i+1][j] = sum[i][j] + triangle[i+1][j];
            }
            if (sum[i+1][j+1] < sum[i][j] + triangle[i+1][j+1]) {
                sum[i+1][j+1] = sum[i][j] + triangle[i+1][j+1];
            }
        }
    }
    int s = triangle.size();
    for (int i = 0; i < triangle[s-1].size(); ++i) {
        // cout << 
        answer = max(answer, sum[s-1][i]);
    }

    return answer;
}


int main() {
    cout << solution({{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}}) << endl;
}