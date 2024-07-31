#include <iostream>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <vector>
#include <queue>

using namespace std;

int dx[8] = { 1, 0, -1, 0 , 1, 1, -1, -1 };
int dy[8] = { 0, 1, 0, -1 , 1, -1, 1, -1 };

int main() {
	int N, M;
	cin >> N >> M;
	vector<vector<bool>> letters;
	vector<bool> t(M, false);
	vector<vector<bool>> visited(N, t);

	for (int i = 0; i < N; i++) {
		vector<bool> tmpLetter;
		for (int j = 0; j < M; j++) {
			int a;
			cin >> a;
			tmpLetter.push_back(a);
		}
		letters.push_back(tmpLetter);
	}
	int answer = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (!letters[i][j] || visited[i][j]) continue;
			queue<int> list;
			list.push(i*M + j);
			visited[i][j] = true;
			answer++;
			while (!list.empty()) {
				int tmpValue = list.front();
				list.pop();
				int x = tmpValue / M, y = tmpValue % M;
				for (int k = 0; k < 8; k++) {
					int nx = x + dx[k], ny = y + dy[k];
					if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
					if (letters[nx][ny] && !visited[nx][ny]) {
						visited[nx][ny] = true;
						list.push(nx*M + ny);
					}
				}
			}
		}
	}
	cout << answer;
	/*
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				cout << letters[i][j] << " ";
			}
			cout << endl;
		}
	*/

	return 0;
}