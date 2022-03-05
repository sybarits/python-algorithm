#include <string>
#include <vector>
#include <iostream>
#include <stack>

using namespace std;

int peekDoll(vector<vector<int>> &board, int num);

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    stack<int> s;

    for (size_t i = 0; i < moves.size(); i++) {
        int doll = peekDoll(board, moves[i]-1);
        if (doll != 0) {
            if (!s.empty() && s.top() == doll) {
                s.pop();
                answer++;
            } else {
                s.push(doll);
            }
        }
    }
    return answer * 2;
}

int peekDoll(vector<vector<int>> &board, int num) {
    for (size_t i = 0; i < board.size(); i++) {
        if (board[i][num] != 0) {
            int answer = board[i][num];
            board[i][num] = 0;
            return answer;
        }
    }
    return 0;
}

int main() {
    cout << solution({{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}},{1,5,3,5,1,2,1,4}) << endl;
}