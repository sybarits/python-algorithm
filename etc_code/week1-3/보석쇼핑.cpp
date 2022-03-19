#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> gems) {
    vector<int> answer;
    map<string, int> gems_map;
    map<string, int> temp_map;

    for (string s: gems) {
        gems_map.insert(pair<string,int>(s,0));
    }
    
    gems.insert(gems.begin(), "");

    int gem_len = gems_map.size();
    int len = gems.size() -1;
    int left = 1;
    int right = 1;
    int a = 0;
    int b = 0;
    int temp_len = len + 1;

    temp_map.clear();
    temp_map.insert(pair<string,int>(gems.at(right),1));
    while (left < len) {

        if (temp_map.size() == gem_len
            && temp_len > right - left + 1) {
                temp_len = right - left + 1;
                a = left;
                b = right;
        } else if (temp_map.size() < gem_len) {
            if (right < len) {
                ++right;
                if (temp_map.find(gems.at(right)) == temp_map.end()) {
                    temp_map.insert(pair<string,int>(gems.at(right),1));
                } else {
                    ++temp_map[gems.at(right)];
                }
            } else {
                break;
            }
        } else {
            if (1 == temp_map[gems.at(left)]) {
                temp_map.erase(gems.at(left));
            } else {
                --temp_map[gems.at(left)];
            }
            ++left;
        }
        // cout << "left " << left << " right " << right << endl;
        // for (auto s = temp_map.begin(); s != temp_map.end(); ++s) {
        //     cout << s->first << " " << s->second << ", ";
        // }
        // cout << endl;
    }

    return {a,b};
}

int main() {
    vector<int> result = solution({"DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"});
    cout << "result " << result[0] << ", " << result[1] << endl;
    result = solution({"AA", "AB", "AC", "AA", "AC"});
    cout << "result " << result[0] << ", " << result[1] << endl;
    result = solution({"XYZ", "XYZ", "XYZ"});
    cout << "result " << result[0] << ", " << result[1] << endl;
    result = solution({"ZZZ", "YYY", "NNNN", "YYY", "BBB"});
    cout << "result " << result[0] << ", " << result[1] << endl;
}