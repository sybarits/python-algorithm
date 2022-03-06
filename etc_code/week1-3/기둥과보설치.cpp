#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool isValid(vector<vector<int>> &answer);
bool validStructur(vector<vector<int>> &answer, int x, int y, int a, int n);
bool removeStruct(vector<vector<int>> &answer, int x, int y, int a);
bool compare(vector<int> a, vector<int> b);

vector<vector<int>> solution(int n, vector<vector<int>> build_frame) {
    vector<vector<int>> answer;

    for (size_t i = 0; i < build_frame.size(); i++) {
        int x = build_frame[i][0];
        int y = build_frame[i][1];
        int a = build_frame[i][2];//0: 기둥, 1: 보
        int b = build_frame[i][3];//0: delete, 1: install

        if ( b == 1) {//install
            if (validStructur(answer, x, y, a, n)) {
                answer.push_back({x,y,a});
            }
        } else {//delete
            if (removeStruct(answer, x, y, a)) {
                if (!isValid(answer)) {
                    answer.push_back({x,y,a});
                }
            }
        }
    }

    sort(answer.begin(), answer.end(), compare);

    // for (size_t i = 0; i < answer.size(); i++) {
    //     for (size_t j = 0; j < answer[i].size(); j++) {
    //         cout << answer[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    
    return answer;
}

bool validStructur(vector<vector<int>> &answer, int x, int y, int a, int n) {
    // cout << x << " " << y << " " << a << endl;
    // 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야한다.
    // 보는 한쪽 끝 부분이 기둥 위헤 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 한다.
    if (a == 0 && y == 0) {
        return true;
    }
    for (size_t i = 0; i < answer.size(); i++) {
        int sx = answer[i][0];
        int sy = answer[i][1];
        int struc = answer[i][2];
        if (a == 0) {
            if (y == 0 ||
                (struc == 1 && sy == y && (sx == x || sx == x-1)) ||
                (struc == 0 && sy == y -1 && sx == x) ) {
                    return true;
            }
        } else {
            if (struc == 0 && sy == y-1 && (sx == x || sx == x+1)) {
                return true;
            }
        }
    }
    int count = 0;
    if (a == 1) {
        for (size_t i = 0; i < answer.size(); i++) {
            int sx = answer[i][0];
            int sy = answer[i][1];
            int struc = answer[i][2];
            if (struc == 1 && sy == y && (sx == x+1 || sx == x-1)) {
                count++;
            }
        }
        if (count == 2) {
            return true;
        }
    }

    
    return false;
}

bool isValid(vector<vector<int>> &answer) {
    bool result = true;
    for (size_t i = 0; i < answer.size(); i++) {
        int x = answer[i][0];
        int y = answer[i][1];
        int a = answer[i][2];
        if (!validStructur(answer, x, y, a, 0)) {
            result = false;
            break;
        }
    }
    return result;
}

bool removeStruct(vector<vector<int>> &answer, int x, int y, int a) {
    for (size_t i = 0; i < answer.size(); i++) {
        if (answer[i][0] == x && answer[i][1] == y && answer[i][2] == a) {
            answer.erase(answer.begin() + i);
            return true;
        }
    }
    return false;
}

bool compare(vector<int> a, vector<int> b) {
    if (a[0] != b[0]) {
        return a[0] < b[0];
    } else {
        if (a[1] != b[1]) {
            return a[1] < b[1];
        } else {
            return a[2] < b[2];
        }
    }
    return false;
}


int main() {
    vector<vector<int>> build_frame = {{1,0,0,1},{1,1,1,1},{2,1,0,1},{2,2,1,1},{5,0,0,1},{5,1,0,1},{4,2,1,1},{3,2,1,1}};
    vector<vector<int>> result = solution(5, build_frame);
    cout << endl;
    vector<vector<int>> build_frame2 = {{0,0,0,1},{2,0,0,1},{4,0,0,1},{0,1,1,1},{1,1,1,1},{2,1,1,1},{3,1,1,1},{2,0,0,0},{1,1,1,0},{2,2,0,1}};
    vector<vector<int>> result2 = solution(5, build_frame2);
}