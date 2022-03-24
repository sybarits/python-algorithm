#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <tuple>

using namespace std;

bool cmp(tuple<string,int,int> a, tuple<string,int,int> b) {
    if (get<1>(a) > get<1>(b)) {
        return true;
    }
    if (get<1>(a) == get<1>(b)) {
        if (get<2>(a) > get<2>(b)) {
            return true;
        }
        if (get<2>(a) == get<2>(b)) {
            if (get<0>(a).compare(get<0>(b)) < 0) {
                return true;
            }
        }
    }
    return false;
}

vector<string> solution(vector<string> company_names, vector<vector<int>> scores) {
    int C = company_names.size();
    vector<string> answer(C);
    vector<tuple<string,int,int>> company_score;
    for (int i = 0; i < C; ++i) {
        int s = 0;
        int sum = 0;
        for (int j = 0; j < scores[i].size(); ++j) {
            if (scores[i][j] >= 80) {
                ++s;
            }
            sum += scores[i][j];
        }
        company_score.push_back(make_tuple(company_names[i], s, sum));
    }
    sort(company_score.begin(), company_score.end(), cmp);

    for (int i = 0; i < C; ++i) {
        answer[i] = (string)get<0>(company_score[i]);
        cout << answer[i] << endl;
    }

    return answer;
}


int main() {
    solution({"warehouse", "parkworld", "eggandbacon", "xyz", "hellomark", "olive"}, {{74,76,65,90,75},{95,70,85,60,65},{75,75,75,75,80},{90,100,85,75,70},{100,79,100,70,79},{70,71,100,80,39}} );
}