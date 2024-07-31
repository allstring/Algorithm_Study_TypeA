#include <iostream>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <vector>
#include <queue>

using namespace std;

int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

int main() {
	int N, M, K;
	cin >> N >> M >> K;
	vector<bool> m(M, false);
	vector<vector<bool>> meals(N, m);
	vector<vector<bool>> visited(N, m);
	for (int i = 0; i < K; i++) {
		int x, y;
		cin >> x >> y;
		meals[x - 1][y - 1] = true;
	}
	int answer = 0;
	queue<int> Queue;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (visited[i][j] || !meals[i][j]) continue;
			queue<int> A;
			visited[i][j] = true;
			A.push(i*M + j);
			int tmpAnswer = 0;
			while (!A.empty()) {
				int tmpValue = A.front();
				A.pop();
				tmpAnswer++;
				int x = tmpValue / M, y = tmpValue % M;
				for (int k = 0; k < 4; k++) {
					int nx = x + dx[k], ny = y + dy[k];
					if (nx < 0 || nx >= N || ny < 0 || ny >= M || visited[nx][ny] || !meals[nx][ny]) continue;
					visited[nx][ny] = true;
					A.push(nx*M + ny);
				}
			}
			answer = answer > tmpAnswer ? answer : tmpAnswer;
		}
	}
	cout << answer;
	return 0;
}