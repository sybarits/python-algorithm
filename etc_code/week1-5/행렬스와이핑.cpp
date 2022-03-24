#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int rows, int columns, vector<vector<int>> swipes) {
    vector<int> answer;
    vector<vector<int>> mat(rows+1);

    for (int i = 1; i <= rows; ++i) {
        for (int j = 0; j <= columns; ++j) {
            mat[i].push_back((i-1) * columns + j);
        }
    }

    for(auto s : swipes) {
        int d = s[0], r_min = s[1], c_min = s[2], r_max = s[3], c_max = s[4];
        int sum = 0, temp = 0;
        if (d == 1) {//down r+1
            for (int c = c_min; c <= c_max; ++c) {
                temp = mat[r_max][c];
                sum += temp;
                for (int r = r_max; r > r_min; --r) {
                    mat[r][c] = mat[r-1][c];
                }
                mat[r_min][c] = temp;
            }
        } else if (d == 2) {//up r-1
            for (int c = c_min; c <= c_max; ++c) {
                temp = mat[r_min][c];
                sum += temp;
                for (int r = r_min; r < r_max; ++r) {
                    mat[r][c] = mat[r+1][c];
                }
                mat[r_max][c] = temp;
            }
        } else if (d == 3) {//left c+1
            for (int r = r_min; r <= r_max; ++r) {
                temp = mat[r][c_max];
                sum += temp;
                for (int c = c_max; c > c_min; --c) {
                    mat[r][c] = mat[r][c-1];
                }
                mat[r][c_min] = temp;
            }
        } else if (d == 4) {//right c-1
            for (int r = r_min; r <= r_max; ++r) {
                temp = mat[r][c_min];
                sum += temp;
                for (int c = c_min; c < c_max; ++c) {
                    mat[r][c] = mat[r][c+1];
                }
                mat[r][c_max] = temp;
            }
        }

        answer.push_back(sum);
    }

    return answer;
}


int main() {
    solution(4,3,{{1,1,2,4,3},{3,2,1,2,3},{4,1,1,4,3},{2,2,1,3,3}});
}