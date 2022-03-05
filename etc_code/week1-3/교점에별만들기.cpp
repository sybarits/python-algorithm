#include <string>
#include <vector>
#include <iostream>
#include <climits>

using namespace std;

string isStar(int x, int y, vector<vector<long int>> &points);

vector<string> solution(vector<vector<int>> line) {
	vector<vector<long int>> points;
	vector<int>::size_type line_size = line.size();
	long int min_x = LLONG_MAX;
	long int max_x = LLONG_MIN;
	long int min_y = LLONG_MAX;
	long int max_y = LLONG_MIN;

	for (vector<int>::size_type i = 0; i < line_size; i++) {
		for (vector<int>::size_type j = i + 1; j < line_size; j++) {
            long int a = line[i][0];
            long int b = line[i][1];
            long int e = line[i][2];
            long int c = line[j][0];
            long int d = line[j][1];
            long int f = line[j][2];
            long int deno = a*d-b*c;
            if (deno == 0) {
                continue;
            }
            long int x = b*f - e*d;
            long int y = e*c - a*f;
			if (x%deno != 0 || y%deno != 0) {
				continue;
			}
			x = x/deno;
			y = y/deno;
            points.push_back({x,y});
			min_x = min(min_x, x);
			min_y = min(min_y, y);
			max_x = max(max_x, x);
			max_y = max(max_y, y);
		}
	}
	string row = string(max_x - min_x + 1, '.');
	vector<string> result(max_y - min_y + 1, row);

	for (vector<long int> xy : points) {
		result[abs(xy[1] - max_y)][abs(xy[0] - min_x)] = '*';
	}
	
    for (size_t i = 0; i < result.size(); i++)
    {
        for (size_t j = 0; j < result[i].size(); j++)
        {
            cout << result[i][j];
        }
        cout << endl;
        
    }
    
	return result;
}


int main() {
    std::cout << " wow " << std::endl;
    vector<vector<int>> points = {{2, -1, 4}, {-2, -1, 4}, {0, -1, 1}, {5, -8, -12}, {5, 8, 12}};
    solution(points);
    long int a = 3;
    long int b = 2;
	string sss = "abcdef";
	sss[3]='o';
    cout << sss << endl;
}