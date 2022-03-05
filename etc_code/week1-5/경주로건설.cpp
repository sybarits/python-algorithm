#include <string>
#include <vector>
#include <iostream>

using namespace std;
int bfs(vector<vector<int>> &board, vector<vector<int>> &price);

int solution(vector<vector<int>> board) {
    int answer = 0;
    vector<int> row(board[0].size(), 999999999);
	vector<vector<int>> price(board.size(), row);

    bfs(board, price);


    for (size_t i = 0; i < price.size(); i++)
    {
        for (size_t j = 0; j < price[i].size(); j++)
        {
            cout << price[i][j] << " ";
        }
        cout << endl;
        
    }

    cout << endl;
    cout << endl;
    return 0;//bfs(board, price);;
}

int bfs(vector<vector<int>> &board, vector<vector<int>> &price) {
    // 0: down, 1: right, 2: up, 3: left
    vector<vector<int>> start;//0: direction, 1: row, 2: col
    vector<vector<int>> end;

     price[0][0] = 0;
    if (board[0][1] == 0) {
        start.push_back({1,0,1});
        price[0][1] = 100;
    }
    if (board[1][0] == 0) {
        start.push_back({0,1,0});
        price[1][0] = 100;
    }
    int row = 0;
    int col = 0;
    int direction = 0;
    int temp_price = 0;
    int board_size = board.size();
    int max_row = board_size - 1;
    int max_col = board_size - 1;

    while (start.size() != 0) {

        for (int i = 0; i < start.size(); i++)
        {
            direction = start[i][0];
            row = start[i][1];
            col = start[i][2];
            
            if (row == max_row && col == max_col) {
                cout << "final " << price[max_row][max_col] << endl;
            }
            //down
            if (row < max_row && board[row+1][col] == 0) {
                if (direction == 0) {
                    temp_price = price[row][col] + 100;
                } else {
                    temp_price = price[row][col] + 600;
                }
                if (temp_price <= price[row+1][col]) {
                    price[row+1][col] = temp_price;
                    end.push_back({0,row+1,col});
                }
            }
            //right
            if (col < max_col && board[row][col+1] == 0) {
                if (direction == 1) {
                    temp_price = price[row][col] + 100;
                } else {
                    temp_price = price[row][col] + 600;
                }
                if (temp_price <= price[row][col+1]) {
                    price[row][col+1] = temp_price;
                    end.push_back({1,row,col+1});
                }
            }
            //up
            if (row > 0 && board[row-1][col] == 0) {
                if (direction == 2) {
                    temp_price = price[row][col] + 100;
                } else {
                    temp_price = price[row][col] + 600;
                }
                if (temp_price <= price[row-1][col]) {
                    price[row-1][col] = temp_price;
                    end.push_back({2,row-1,col});
                }
            }
            //left
            if (col > 0 && board[row][col-1] == 0) {
                if (direction == 3) {
                    temp_price = price[row][col] + 100;
                } else {
                    temp_price = price[row][col] + 600;
                }
                if (temp_price <= price[row][col-1]) {
                    price[row][col-1] = temp_price;
                    end.push_back({3,row,col-1});
                }
            }
        }
        start = end;
        end.clear();
    }

    return price[max_row][max_col];
}

int main() {
    // vector<vector<int>> board1 = {{0,0,0},{0,0,0},{0,0,0}};
    // solution(board1);//900
    // vector<vector<int>> board2 = {{0,0,0,0,0,0,0,1},{0,0,0,0,0,0,0,0},{0,0,0,0,0,1,0,0},{0,0,0,0,1,0,0,0},{0,0,0,1,0,0,0,1},{0,0,1,0,0,0,1,0},{0,1,0,0,0,1,0,0},{1,0,0,0,0,0,0,0}};
    // solution(board2);//3800
    // vector<vector<int>> board3 = {{0,0,1,0},{0,0,0,0},{0,1,0,1},{1,0,0,0}};
    // solution(board3);//2100
    // vector<vector<int>> board4 = {{0,0,0,0,0,0},{0,1,1,1,1,0},{0,0,1,0,0,0},{1,0,0,1,0,1},{0,1,0,0,0,1},{0,0,0,0,0,0}};
    // solution(board4);//3200
    vector<vector<int>> board5 = {{0, 0, 0, 0, 0},{0, 1, 1, 1, 0},{0, 0, 1, 0, 0},{1, 0, 0, 0, 1},{0, 1, 1, 0, 0}};
    cout << solution(board5) << endl;//3000

}