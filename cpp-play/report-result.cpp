#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>
#include <set>

using namespace std;

//프로그래머스 문제 풀이
//https://programmers.co.kr/learn/courses/30/lessons/92334?language=cpp

vector<string> split(string str, char Delimiter) {
    istringstream iss(str);             // istringstream에 str을 담는다.
    string buffer;                      // 구분자를 기준으로 절삭된 문자열이 담겨지는 버퍼

    vector<string> result;

    // istringstream은 istream을 상속받으므로 getline을 사용할 수 있다.
    while (getline(iss, buffer, Delimiter)) {
        result.push_back(buffer);               // 절삭된 문자열을 vector에 저장
    }

    return result;
}

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer;
    map<string, set<string>> report_map;
    map<string, int> report_cnt;

    for (string r : report) {
        vector<string> rr = split(r, ' ');
        if (report_map.find(rr[0]) == report_map.end()) {
            set<string> temp_set;
            temp_set.insert(rr[1]);
            report_map.insert({ rr[0],temp_set });
        }
        else {
            report_map[rr[0]].insert(rr[1]);
        }


    }
    map<string, set<string>>::iterator iter;
    for (iter = report_map.begin(); iter != report_map.end(); iter++) {
        set<string>::iterator map_iter;
        for (map_iter = iter->second.begin(); map_iter != iter->second.end(); map_iter++) {
            if (report_cnt.find(*map_iter) == report_cnt.end()) {
                report_cnt.insert({ *map_iter, 1 });
            }
            else {
                ++report_cnt[*map_iter];
            }
        }

    }

    for (string id : id_list) {
        int temp_cnt = 0;
        set<string>::iterator map_iter;
        for (map_iter = report_map[id].begin(); map_iter != report_map[id].end(); map_iter++) {
            if (report_cnt[*map_iter] >= k) {
                ++temp_cnt;
            }
        }
        answer.push_back(temp_cnt);
    }


    for (int i : answer) {
        cout << i << endl;
    }
    return answer;
}


int main() {
    solution({ "muzi", "frodo", "apeach", "neo" }, { "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi" }, 2);
    
}