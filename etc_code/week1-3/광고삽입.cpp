#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string sec2time(int sec) {
    string result = "";
    int temp = sec / 3600;
    if (temp == 0) {
        result = "00:";
    } else if (temp / 10 > 0) {
        result = (to_string(temp)+":");
    } else {
        result = "0"+to_string(temp)+":";
    }

    temp = sec % 3600;
    temp /= 60;
    if (temp == 0) {
        result += "00:";
    } else if (temp / 10 > 0) {
        result += (to_string(temp)+":");
    } else {
        result += "0"+to_string(temp)+":";
    }

    temp = sec % 60;
    if (temp == 0) {
        result += "00";
    } else if (temp / 10 > 0) {
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
    if (a[0] > b[0]) {
        return true;
    }
    return false;
}

int cnt[360000];

string solution(string play_time, string adv_time, vector<string> logs) {
    string answer = "";
    vector<string> temp;
    int play = time2sec(play_time);
    int adv = time2sec(adv_time);
    vector<vector<int>> int_logs;

    // cout << "full play time " << play_time << " " << play << " adv time " << adv << endl;
    for (size_t i = 0; i < logs.size(); i++) {
        int_logs.push_back({time2sec(logs[i].substr(0,8)),time2sec(logs[i].substr(9,8))});
    }
    int_logs.push_back({0,0});
    sort(int_logs.begin(), int_logs.end(), cmp);
    long long max_time = play;
    long long max_sum = 0;
    
    for (size_t j = 0; j < int_logs.size(); j++)
    {
        int ad_start = int_logs[j][0];
        int ad_end = ad_start + adv;
        long long  temp_sum = 0;
        if (ad_end > play) {
            ad_end = play;
        }
        for (size_t i = 0; i < int_logs.size(); i++) {
            if (ad_start <= int_logs[i][0] && ad_end >= int_logs[i][1] ||
                ad_start >= int_logs[i][0] && ad_start <= int_logs[i][1] ||
                ad_end >= int_logs[i][0] && ad_end <= int_logs[i][1] ) {
                int start = max(ad_start, int_logs[i][0]);
                int end = min(ad_end, int_logs[i][1]);
                temp_sum += (end-start);
            }
        }
        
        if (max_sum <= temp_sum) {
            max_sum = temp_sum;
            max_time = ad_start;
        }
        // cout << "start sec " << ad_start << " start time " << sec2time(ad_start) << " temp_sum " << temp_sum << endl;
    }

    return sec2time(max_time);
}


int main() {
    cout << "answer is " <<  solution("02:03:55", "00:14:15", {"01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"}) << endl;
    cout << "answer is " <<  solution("99:59:59", "25:00:00", {"69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"}) << endl;
    cout << "answer is " << solution("50:00:00", "50:00:00", {"15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"}) << endl;
}