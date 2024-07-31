#include <iostream>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <vector>
#include <queue>

using namespace std;

int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

bool checker(vector<vector<char>> classes, int N) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (classes[i][j] != 'T') continue;
			for (int k = 0; k < 4; k++) {
				int nx = i, ny = j;
				while (true) {
					nx += dx[k], ny += dy[k];
					if (nx < 0 || nx >= N || ny < 0 || ny >= N || classes[nx][ny] == 'O') break;
					if (classes[nx][ny] == 'S') return false;
				}
			}
		}
	}
	return true;
}


int main() {
	int N;
	cin >> N;
	vector<vector<char>> classes;

	for (int i = 0; i < N; i++) {
		vector<char> tmpClass;
		for (int j = 0; j < N; j++) {
			char A;
			cin >> A;
			tmpClass.push_back(A);
		}
		classes.push_back(tmpClass);
	}

	for (int i = 0; i < N*N - 2; i++) {
		int x1 = i / N, y1 = i % N;
		if (classes[x1][y1] != 'X') continue;
		classes[x1][y1] = 'O';
		for (int j = i + 1; j < N*N - 1; j++) {
			int x2 = j / N, y2 = j % N;
			if (classes[x2][y2] != 'X') continue;
			classes[x2][y2] = 'O';
			for (int k = j + 1; k < N*N; k++) {
				int x3 = k / N, y3 = k % N;
				if (classes[x3][y3] != 'X') continue;
				classes[x3][y3] = 'O';
				if (checker(classes, N)) {
					cout << "YES";
					return 0;
				}
				classes[x3][y3] = 'X';
			}
			classes[x2][y2] = 'X';

		}
		classes[x1][y1] = 'X';
	}

	cout << "NO";
	return 0;
}