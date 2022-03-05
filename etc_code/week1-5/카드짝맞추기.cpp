#include <string>
#include <vector>
#include <deque>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> findCardPosition(vector<vector<int>> &board, int start_r, int start_c);
vector<int> findMinimumCostCard(vector<vector<int>> &board, int start_r, int start_c);
int dfs(vector<vector<int>> &board, int start_r, int start_c, int end_r, int end_c, int this_cost);
int getCost(vector<vector<int>> &board, int start_r, int start_c, int end_r, int end_c);
bool isCard(vector<vector<int>> &board);
bool cmp(vector<int> a, vector<int> b);

vector<vector<int>> cards;
int cost = 100;

int solution(vector<vector<int>> board, int r, int c) {
    int answer = 0;
    int start_r = r;
    int start_c = c;

    while (isCard(board)) {
        cost = 100;
        int start_card = board[start_r][start_c];
        // cout << "start " << start_r << " " <<  start_c << endl;
        if (start_card == 0) {
            vector<int> end_card = findMinimumCostCard(board, start_r, start_c);
            answer += end_card[0];
            start_r = end_card[1];
            start_c = end_card[2];
        } else {
            vector<int> end_card_position = findCardPosition(board, start_r, start_c);
            int card_cost = getCost(board, start_r, start_c, end_card_position[0], end_card_position[1]);
            answer += (card_cost + 2);
            board[end_card_position[0]][end_card_position[1]] = 0;
            start_r = end_card_position[0];
            start_c = end_card_position[1];
        }
    }

    return answer;
}

bool isCard(vector<vector<int>> &board) {
    for (size_t i = 0; i < board.size(); i++) {
        for (size_t j = 0; j < board[i].size(); j++) {
            if (board[i][j] != 0) {
                return true;
            }
        }
    }
    return false;
    
}
vector<int> findMinimumCostCard(vector<vector<int>> &board, int start_r, int start_c) {
    cards = {};
    vector<vector<int>> result;
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[i].size(); j++) {
            if (board[i][j] != 0) {
                cards.push_back({i,j});
            }
        }
    }

    for (size_t i = 0; i < cards.size(); i++) {
        int temp_cost = getCost(board,start_r,start_c,cards[i][0],cards[i][1]);
        result.push_back({temp_cost, cards[i][0], cards[i][1]});
    }
    sort(result.begin(), result.end(), cmp);
    return result[0];//{cost, row, col}
}

bool cmp(vector<int> a, vector<int> b) { 
	return a[0] < b[0]; 
} 

vector<int> findCardPosition(vector<vector<int>> &board, int start_r, int start_c) {
    vector<pair<int,int>> start;
    vector<pair<int,int>> end;
    int start_card = board[start_r][start_c];
    vector<vector<int>> visit(4,vector<int>(4,0));
    int row, col;
    
    start.push_back({start_r,start_c});
    visit[start_r][start_c] = 1;
    board[start_r][start_c] = 0;

    while (start.size() != 0) {
        end.clear();
        for (size_t i = 0; i < start.size(); i++) {
            row = start[i].first;
            col = start[i].second;
            // cout << "start " << row << " " << col << endl;
            if (start_card == 0 && board[row][col] != 0 ) {
                return {row,col};
            }
            if (start_card != 0 && board[row][col] == start_card) {
                return {row,col};
            }
            if (row < 3 && visit[row+1][col] == 0) {
                end.push_back({row+1,col});
                visit[row+1][col] = 1;
            }
            if (row > 0 && visit[row-1][col] == 0) {
                end.push_back({row-1,col});
                visit[row-1][col] = 1;
            }
            if (col < 3 && visit[row][col+1] == 0) {
                end.push_back({row,col+1});
                visit[row][col+1] = 1;
            }
            if (col > 0 && visit[row][col-1] == 0) {
                end.push_back({row,col-1});
                visit[row][col-1] = 1;
            }
        }
        for (size_t i = 0; i < end.size(); i++) {
            visit[end[i].first][end[i].second] = 1;
        }
        start.clear();
        start = end;
    }

    return {row,col};
}

int getCost(vector<vector<int>> &board, int start_r, int start_c, int end_r, int end_c) {
    dfs(board, start_r, start_c, end_r, end_c, 0);
    return cost;
}

int dfs(vector<vector<int>> &board, int start_r, int start_c, int end_r, int end_c, int this_cost) {
    // cout << "dfs call " << start_r << " " <<  start_c << " " << end_r << " " << end_c << endl;
    // cout << "cost " << this_cost << endl;
    if (this_cost >= cost) {
        return 0;
    }
    if (start_r == end_r && start_c == end_c) {
        if (this_cost < cost) {
            cost = this_cost;
            // cout << "end cost " << this_cost << endl;
        }
        return this_cost;
    }
    int max_r = max(start_r, end_r);
    int min_r = min(start_r, end_r);
    int max_c = max(start_c, end_c);
    int min_c = min(start_c, end_c);
    
    if (start_r < end_r) {

    }
    //down
    if (start_r <= end_r && start_r < max_r) {
        //go down
        int down = start_r + 1;
        while (board[down][start_c] == 0 && down < max_r) {
            down++;
        }
        dfs(board, down, start_c, end_r, end_c, this_cost+1);
    }
    //up
    if (start_r >= end_r && start_r > min_r) {
        //go up
        int up = start_r - 1;
        while (board[up][start_c] == 0 && up > min_r) {
            up--;
        }
        dfs(board, up, start_c, end_r, end_c, this_cost+1);
    }
    //left
    if (start_c >= end_c && start_c > min_c) {
        //go left
        int left = start_c - 1;
        while (board[start_r][left] == 0 && left > min_c) {
            left--;
        }
        dfs(board, start_r, left, end_r, end_c, this_cost+1);
    }
    //right
    if (start_c <= end_c && start_c < max_c) {
        //go right
        int right = start_c + 1;
        while (board[start_r][right] == 0 && right < max_c) {
            right++;
        }
        dfs(board, start_r, right, end_r, end_c, this_cost+1);
    }
}

int main() {

    vector<vector<int>> board ={{1,0,0,3},{2,0,0,0},{0,0,0,2},{3,0,1,0}};
    vector<vector<int>> board3 ={{1,0,0,3},{2,0,0,0},{0,0,0,2},{3,0,1,0}};
    // vector<int> card = findCardPosition(board, 0, 0);
    // cout << "card!! " << card[0] << " " << card[1] << endl;
    // int rr = getCost(board, 0, 0, 3, 2);
    // cout << "cost " << rr << endl;
    // rr = getCost(board, 1, 0, 2, 3);
    // cout << "cost " << rr << endl;
    // rr = getCost(board, 0, 1, 0, 0);
    // cout << "cost " << rr << endl;

    int result = solution(board, 1, 0);
    cout << result << endl;

    vector<vector<int>> board2 ={{3,0,0,2},{0,0,1,0},{0,1,0,0},{2,0,0,3}};
    result = solution(board2, 0, 1);
    cout << result << endl;
}