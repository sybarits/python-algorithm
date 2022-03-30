#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

string solution(string s) {
    string answer;
    vector<char> st;
    
    for (char c : s) {
        while (st.size() != 0 && st.back() < c ) {
            st.pop_back();
        }
        st.push_back(c);
    }

    for (char c : st) {
        answer += c;
    }
    
    return answer;
}

int main() {
    cout << "answer " << solution("xyb") << endl; 
    string path = "..\\lexical-substring_tests_improved\\";
    for (int i = 1; i != 101; ++i) {
        ifstream ifs_input;
        ifstream ifs_answer;
        if (i<10) {
            ifs_input.open(path+"0"+to_string(i));
            ifs_answer.open(path+"0"+to_string(i)+".a");
        } else {
            ifs_input.open(path+to_string(i));
            ifs_answer.open(path+to_string(i)+".a");
        }

        char c;
        string input = "";
        while (ifs_input.get(c)) {
            input += c;
        }

        string answer = "";
        while (ifs_answer.get(c)) {
            answer += c;
        }
        string result = solution(input);
        input[input.length() - 1] = '\0';
        answer += '\0';
        result[result.length() - 1] = '\0';
        
        if (answer.compare(result) == 0) {
            cout << i << " " << "true" << endl;
        } else {
            cout << i << " " << "false" << endl;
        }

    }
    
}