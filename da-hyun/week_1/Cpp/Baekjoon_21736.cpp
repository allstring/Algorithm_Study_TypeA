#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<char>> school;
vector<vector<bool>> visited;
int answer = 0;
int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };
int N, M;
void recursive(int x, int y) {
	if (x < 0 || x >= N || y < 0 || y >= M || visited[x][y] || school[x][y] == 'X') return;

	if (school[x][y] == 'P') answer++;
	visited[x][y] = true;

	for (int i = 0; i < 4; i++) recursive(x + dx[i], y + dy[i]);
	return;
}

int main() {

	cin >> N >> M;
	vector<bool> tmpVisited(M, false);
	int x, y;
	for (int i = 0; i < N; i++) {
		visited.push_back(tmpVisited);
		vector<char> tmpSchool;
		for (int j = 0; j < M; j++) {
			char a;
			cin >> a;
			if (a == 'I') {
				x = i;
				y = j;
			}
			tmpSchool.push_back(a);
		}
		school.push_back(tmpSchool);
	}
	recursive(x, y);
	cout << (answer ? to_string(answer) : "TT") << endl;

	return 0;
}