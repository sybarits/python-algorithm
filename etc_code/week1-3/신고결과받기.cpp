#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

vector<string> split(string s, string delimeter);

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer;
    map<string, vector<string>> report_map;//신고한 id | 신고당한 id
    map<string,int> stop_id;//id 당 신고당한 수
    map<string,int> mail_result;//신고한 id | 받은 메일 수

    for (size_t i = 0; i < id_list.size(); i++) {
        report_map.insert(pair<string, vector<string>>(id_list[i],{}));
        mail_result.insert(pair<string,int>(id_list[i],0));
        stop_id.insert(pair<string,int>(id_list[i],0));
    }

    for (size_t i = 0; i < report.size(); i++){
        vector<string> temp = split(report[i]," ");
        vector<string> report_string = report_map[temp[0]];
        if (find(report_string.begin(), report_string.end(), temp[1]) == report_string.end()) {
            report_map[temp[0]].push_back(temp[1]);
        }
    }
    
    //신고 수 카운트
    for (size_t i = 0; i < id_list.size(); i++) {
        vector<string> v_id = report_map[id_list[i]];
        for (size_t j = 0; j < v_id.size(); j++) {
            stop_id[v_id[j]]++;
        }
    }

    //받은 메일 수 카운트
    for (size_t i = 0; i < id_list.size(); i++) {
        vector<string> v_id = report_map[id_list[i]];
        for (size_t j = 0; j < v_id.size(); j++) {
            if (stop_id[v_id[j]] >= k) {
                mail_result[id_list[i]]++;
            }
        }
    }

    for (size_t i = 0; i < id_list.size(); i++) {
        answer.push_back(mail_result[id_list[i]]);
        cout << id_list[i] << " " << mail_result[id_list[i]] << endl;
    }
    
    return answer;
}


vector<string> split(string s, string delimeter) {
	vector<string> v;
	int start = 0;
	int d = s.find(delimeter);
	while (d != -1){
		v.push_back(s.substr(start, d - start));
		start = d + 1;
		d = s.find(delimeter, start);
	} 
	v.push_back(s.substr(start, d - start));

	return v;
}

int main() {

    solution({"muzi", "frodo", "apeach", "neo"},{"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"},2);
    cout << endl;
    solution({"con", "ryan"}, {"ryan con", "ryan con", "ryan con", "ryan con"}, 3);
}