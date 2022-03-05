#include <string>
#include <vector>
#include <iostream>




using namespace std;

int rotateNum(vector<vector<int>> &m, vector<int>& q);

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
	vector<vector<int>> m;
	
	for (int row = 0; row < rows; row++) {
		m.push_back({});
		for (int column = 0; column < columns; column++) {
			m[row].push_back(row * columns + column + 1);
		}
	}

	for (int row = 0; row < rows; row++) {
		for (int column = 0; column < columns; column++) {
			cout << m[row][column] << " ";
		}
		cout << endl;
	}
	for (size_t i = 0; i < queries.size(); i++)
	{
		answer.push_back(rotateNum(m, queries[i]));
	}
	for (int row = 0; row < rows; row++) {
		for (int column = 0; column < columns; column++) {
			cout << m[row][column] << " ";
		}
		cout << endl;
	}
    return answer;
}

int rotateNum(vector<vector<int>> &m, vector<int> &q) {
	int row1 = q[0] -1;
	int column1 = q[1]-1;
	int row2 = q[2]-1;
	int column2 = q[3]-1;
	int temp1, temp2, temp_r, temp_c;
	int min_temp = m.size() * m[0].size();

	temp_r = row1;
	temp_c = column1;
	temp1 = m[row1][temp_c];
	while (temp_c < column2) {
		min_temp = min(min_temp, temp1);
		temp_c++;
		temp2 = m[row1][temp_c];
		m[row1][temp_c] = temp1;
		temp1 = temp2;
	}
	while (temp_r < row2) {
		min_temp = min(min_temp, temp1);
		temp_r++;
		temp2 = m[temp_r][column2];
		m[temp_r][column2] = temp1;
		temp1 = temp2;
	}
	while (temp_c > column1) {
		min_temp = min(min_temp, temp1);
		temp_c--;
		temp2 = m[row2][temp_c];
		m[row2][temp_c] = temp1;
		temp1 = temp2;
	}
	while (temp_r > row1) {
		min_temp = min(min_temp, temp1);
		temp_r--;
		temp2 = m[temp_r][column1];
		m[temp_r][column1] = temp1;
		temp1 = temp2;
	}

	return min_temp;
}

int main() {
	solution(6, 6, { {2, 2, 5, 4},{3, 3, 6, 6},{5, 1, 6, 3} });
}