#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<bool>> cabages;
vector<vector<bool>> visited;
int answer = 0;
int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };
int N, M, K;
void recursive(int x, int y) {
	if (x < 0 || x >= N || y < 0 || y >= M || visited[x][y] || !cabages[x][y]) return;
	visited[x][y] = true;
	for (int i = 0; i < 4; i++) recursive(x + dx[i], y + dy[i]);
	return;
}

int main() {
	int T;
	cin >> T;
	for (int test_case = 0; test_case < T; test_case++) {
		cabages.clear();
		visited.clear();
		cin >> N >> M >> K;
		vector<bool> tmpVisited(M, false);
		vector<bool> cabage(M, false);

		for (int i = 0; i < N; i++) {
			visited.push_back(tmpVisited);
			cabages.push_back(cabage);
		}
		int x, y;
		for (int i = 0; i < K; i++) {
			cin >> x >> y;
			cabages[x][y] = true;
		}
		int answer = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (cabages[i][j] && !visited[i][j]) {
					answer++;
					recursive(i, j);
				}
			}
		}
		cout << answer << endl;
	}
	return 0;
}