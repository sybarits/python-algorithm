#include<vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> maps) {
    int answer = 0;
    int row_size = maps.size();
    int col_size = maps[0].size();
    int node_size = row_size * col_size;
    int row = 0;
    int col = 0;
    vector<vector<int>> start;
    vector<vector<int>> end;
    bool finish = false;
    
    start.push_back({row,col});
    maps[row][col] = 0;

    do {
        end.clear();
        for (size_t i = 0; i < start.size(); i++) {
            row = start[i][0];
            col = start[i][1];
            if (row == row_size-1 && col == col_size-1) {
                finish = true;
                break;
            }
            //down
            if (row < row_size - 1 && maps[row+1][col] == 1) {
                maps[row+1][col] = 0;
                end.push_back({row+1, col});
            }
            //right
            if (col < col_size - 1 && maps[row][col+1] == 1) {
                maps[row][col+1] = 0;
                end.push_back({row, col+1});
            }
            // up
            if (row > 0 && maps[row-1][col] == 1) {
                maps[row-1][col] = 0;
                end.push_back({row-1, col});
            }
            //left
            if (col > 0 && maps[row][col-1] == 1) {
                maps[row][col-1] = 0;
                end.push_back({row, col-1});
            }
        }

        start = end;
        answer++;
        
    } while (!finish && !start.empty() && answer <= node_size);

    if (!finish || answer > node_size) {
        return -1;
    }

    return answer;

}

int main() {

    cout << solution({{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,1},{0,0,0,0,1}}) << endl;//11
    cout << solution({{1,0,1,1,1,0},{1,0,1,0,1,1},{1,0,1,1,1,0},{1,1,1,0,1,1,0},{0,0,0,0,1,1,1}}) << endl;//12
    cout << solution({{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,0},{0,0,0,0,1}}) << endl;//-1
}