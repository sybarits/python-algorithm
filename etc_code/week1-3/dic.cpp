#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <cstring>

using namespace std;

int solution(string word) {
	int answer = 0;
	//char* word_char = (char*)malloc( word.length() + 1);
	char word_char[6];
	strcpy_s(word_char, word.c_str());
	
	map<char, int> W;
	W.insert(pair<char, int>('A', 0));
	W.insert(pair<char, int>('E', 1));
	W.insert(pair<char, int>('I', 2));
	W.insert(pair<char, int>('O', 3));
	W.insert(pair<char, int>('U', 4));

	int change_word[5];
	change_word[0] = 5 + 5 * 5 + 5 * 5 * 5 + 5 * 5 * 5 * 5 + 1;
	change_word[1] = 5 + 5 * 5 + 5 * 5 * 5 + 1;
	change_word[2] = 5 + 5 * 5 + 1;
	change_word[3] = 5 + 1;
	change_word[4] = 1;

	for (int i = 0; i < word.length(); i++) {
		answer += W[word_char[i]] * change_word[i] + 1;
	}

	return answer;
}

int main() {
	cout << "AAAE result " << solution("AAAE") << endl;
	cout << "I result " << solution("I") << endl;
	cout << "EIO result " << solution("EIO") << endl;
}