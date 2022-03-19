#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

string sec2time(int sec) {
    string result = "";
    int temp = sec / 3600;
    if (temp / 10 > 0) {
        result = (to_string(temp)+":");
    } else {
        result = "0"+to_string(temp)+":";
    }
    temp = sec % 3600;
    temp /= 60;
    if (temp / 10 > 0) {
        result += (to_string(temp)+":");
    } else {
        result += "0"+to_string(temp)+":";
    }
    temp = sec % 60;
    if (temp / 10 > 0) {
        result += (to_string(temp));
    } else {
        result += "0"+to_string(temp);
    }

    return result;
}

int time2sec(string time) {
    int sec = 0;
    int temp_sec = 0;
    temp_sec = (time[0] -'0')*10+(time[1]-'0');
    sec = temp_sec*3600;
    temp_sec = (time[3] -'0')*10+(time[4]-'0');
    sec += temp_sec*60;
    temp_sec = (time[6] -'0')*10+(time[7]-'0');
    sec += temp_sec;
    return sec;
}

bool cmp (vector<int> a, vector<int> b) {
    if (a[0] < b[0]) {
        return true;
    }
    return false;
}

int ad[360000];

string solution(string play_time, string adv_time, vector<string> logs) {
    string answer = "";
    int play = time2sec(play_time);
    int adv = time2sec(adv_time);

    for(string s:logs){
        int start = time2sec(s.substr(0,8));
        int finish = time2sec(s.substr(9,8));
        for(int i=start;i<finish;i++) ad[i]++; // 시청자 수 누적
    }

    int max_time = 0;    
    long long max_sum = 0;
    long long sum = 0;
    queue<int> q;

    for(int i=0;i<adv;i++){
        sum+=ad[i];
        q.push(ad[i]);
    }
    max_sum=sum;

    // 큐를 이용한 투 포인터
    for(int i=adv;i<play;i++){
        sum += ad[i];
        q.push(ad[i]);
        sum -= q.front();
        q.pop();
        if(sum > max_sum){
            max_time = i-adv+1;
            max_sum = sum;
        }
    }

    return sec2time(max_time);
}


int main() {
    cout << "answer is " <<  solution("02:03:55", "00:14:15", {"01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"}) << endl;
    cout << "answer is " <<  solution("99:59:59", "25:00:00", {"69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"}) << endl;
    cout << "answer is " << solution("50:00:00", "50:00:00", {"15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"}) << endl;
}