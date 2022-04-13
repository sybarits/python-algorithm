#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string,int> p_map;

    for (string pp : participant) {
        if (p_map.find(pp) == p_map.end()) {
            p_map.insert(pair<string,int>(pp,1));
        } else {
            ++p_map[pp];
        }
    }

    for (auto i = p_map.begin(); i != p_map.end(); ++i) {
        cout << i->first << " " << i->second << endl;
    }
    

    for (string cc : completion) {
        --p_map[cc];
        if (p_map[cc] == 0) {
            p_map.erase(cc);
        }
    }
    auto ppp = p_map.begin();
    // ++ppp;
    cout << "answer " << ppp->first << endl;
    return ppp->first;
}


int main() {
    solution({"leo", "kiki", "eden"}, {"eden", "kiki"});

}