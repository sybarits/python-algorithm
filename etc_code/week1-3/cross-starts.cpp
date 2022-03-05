#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> getCrossPoint(vector<int> &l1, vector<int> &l2);
vector<int> getMinMaxCoord(vector<vector<int>> &points);
vector<string> getPicture(vector<vector<int>> &points, vector<int> &minmax);
string isStar(int x, int y, vector<vector<int>> &points);

vector<string> solution(vector<vector<int>> line) {
	vector<int> p;
	vector<vector<int>> points;
	vector<int>::size_type line_size = line.size();

	for (vector<int>::size_type i = 0; i < line_size; i++) {
		for (vector<int>::size_type j = i + 1; j < line_size; j++) {
			p = getCrossPoint(line[i], line[j]);
			if (p.size() != 0) {
				points.push_back(p);
			}
		}
	}
	vector<int> minmax = getMinMaxCoord(points);
	return getPicture(points, minmax);
}

vector<int> getCrossPoint(vector<int> &l1, vector<int> &l2) {
	vector<int> result;
	double denominator = l1[0] * l2[1] - l1[1] * l2[0];
	if (denominator == 0) {
		return result;
	}
	double x_numerator = l1[1] * l2[2] - l1[2] * l2[1];
	double y_numerator = l1[2] * l2[0] - l1[0] * l2[2];
	double x = x_numerator / denominator;
	double y = y_numerator / denominator;
	if ((x - int(x) == 0) && (y - int(y) == 0)) {
		return { int(x),int(y) };
	}
	return result;
}

vector<int> getMinMaxCoord(vector<vector<int>> &points) {
	vector<int> result;
	int min_x = 1000;
	int max_x = -1000;
	int min_y = 1000;
	int max_y = -1000;
	for (vector<int>::size_type i = 0; i < points.size(); i++) {
		if (min_x > points[i][0]) {
			min_x = points[i][0];
		}
		if (max_x < points[i][0]) {
			max_x = points[i][0];
		}
		if (min_y > points[i][1]) {
			min_y = points[i][1];
		}
		if (max_y < points[i][1]) {
			max_y = points[i][1];
		}
	}
	result.push_back(min_x);
	result.push_back(max_x);
	result.push_back(min_y);
	result.push_back(max_y);

	return result;//0: min_x, 1: max_x, 2: min_y, 3: max_y
}

vector<string> getPicture(vector<vector<int>> &points, vector<int> &minmax) {
	vector<string> result = {};
	const int min_x = minmax[0];
	const int max_x = minmax[1];
	const int min_y = minmax[2];
	const int max_y = minmax[3];
	
	const int x_size = max_x - min_x + 1;
	const int y_size = max_y - min_y + 1;
	
	string temp;
	for (int y = min_y; y <= max_y; y++) {
		temp = "";
		for (int x = min_x; x <= max_x; x++) {
			temp += isStar(x, y, points);

		}
		//result.push_back(temp);
		result.insert(result.begin(), temp);
	}

	for (size_t j = 0; j < result.size(); j++) {
		cout << result[j] << endl;
	}
	for (vector<int>::size_type k = 0; k < points.size(); k++) {
		cout << points[k][0] << " " << points[k][1] << endl;
	}
	return result;
}

string isStar(int x, int y, vector<vector<int>> &points) {
	for (vector<int>::size_type k = 0; k < points.size(); k++) {
		if (x == points[k][0] && y == points[k][1]) {
			points.erase(points.begin() + k);
			return "*";
		}
	}
	return ".";
}

int main() {
	vector<string> result = solution({ {2, -1, 4}, {-2, -1, 4}, {0, -1, 1}, {5, -8, -12}, {5, 8, 12} });
	solution({ {0, 1, -1},{1, 0, -1},{1, 0, 1} });
	solution({ {1, -1, 0},{2, -1, 0 }, { 4, -1, 0 } });
}

