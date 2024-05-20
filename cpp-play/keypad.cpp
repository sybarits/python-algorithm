#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;



int getDistance(map<char,pair<int,int>> &m, char num1, char num2) {
    int x1 = m[num1].first;
    int y1 = m[num1].second;
    int x2 = m[num2].first;
    int y2 = m[num2].second;    
    // cout << x1 << y1 << x2 << y2 << endl;
    int result = abs(x1 - x2) + abs(y1 - y2);
    return result;
}

string getHand(map<char,pair<int,int>> &m, char L_pos, char R_pos, char currentNum, string hand) {
    int l_distance = getDistance(m, L_pos, currentNum);
    int r_distance = getDistance(m, R_pos, currentNum);

    if (l_distance < r_distance) {
        return "L";
    } else if (l_distance > r_distance) {
        return "R";
    } else {
        if (hand.compare("right") == 0) {
            return "R";
        } else if (hand.compare("left") == 0) {
            return "L";
        }
    }
    return "";
}

string solution(vector<int> numbers, string hand) {
    string answer = "";

    map<char,pair<int,int>> m;
    m.insert({'1',make_pair<int,int>(0,0)});
    m.insert({'2',make_pair<int,int>(0,1)});
    m.insert({'3',make_pair<int,int>(0,2)});
    m.insert({'4',make_pair<int,int>(1,0)});
    m.insert({'5',make_pair<int,int>(1,1)});
    m.insert({'6',make_pair<int,int>(1,2)});
    m.insert({'7',make_pair<int,int>(2,0)});
    m.insert({'8',make_pair<int,int>(2,1)});
    m.insert({'9',make_pair<int,int>(2,2)});
    m.insert({'*',make_pair<int,int>(3,0)});
    m.insert({'0',make_pair<int,int>(3,1)});
    m.insert({'#',make_pair<int,int>(3,2)});

    
    char current_pos_L = '*';
    char current_pos_R = '#';
    for (int num : numbers) {
        if (num == 1 || num == 4 || num == 7) {
            answer += "L";
            current_pos_L = (char)(num+48);
        } else if (num == 3 || num == 6 || num == 9) {
            answer += "R";
            current_pos_R = (char)(num+48);
        } else {
            if (getHand(m,current_pos_L,current_pos_R,(char)(num+48),hand).compare("L") == 0) {
                answer += "L";
                current_pos_L = (char)(num + 48);
            } else {
                answer += "R";
                current_pos_R = (char)(num + 48);
            }
        }
    }
    // cout << answer << endl;
    return answer;
}


int main(){
    solution({1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5},"right");
    solution({7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2},"left");
    // solution({1, 2, 3, 4, 5, 6, 7, 8, 9, 0},"right");
}