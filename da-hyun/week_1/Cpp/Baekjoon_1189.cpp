//
//  Baekjoon_1189.cpp
//  algorithmStudy
//
//  Created by TeamGonom on 8/3/24.
//
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int recursive(int x, int y, int depth, bool** board, bool** visited, int N, int M, int K){
    if((x == 0 && y == M-1) || depth == K){
        if((x == 0 && y == M-1) && depth == K){
            return 1;
        }
        return 0;
    }
    visited[x][y] = true;
    int tmpAnswer = 0;
    for(int i=0;i<4;i++){
        int nx = x + dx[i], ny = y + dy[i];
        if(nx < 0 || ny < 0 || nx>=N || ny >= M || visited[nx][ny] || !board[nx][ny]) continue;
        tmpAnswer += recursive(nx, ny, depth+1, board, visited, N, M, K);
    }
    visited[x][y] = false;
    return tmpAnswer;
}

int main(){
    int N, M, K;
    cin >> N >> M >> K;
    bool ** visited, ** map;
    map = new bool*[N];
    visited = new bool*[N];
    for(int i=0;i<N;i++){
        map[i] = new bool[N];
        visited[i] = new bool[N];
        for(int j=0;j<M;j++){
            char A;
            cin >> A;
            map[i][j] = (A == '.');
            visited[i][j] = false;
        }
    }
    cout << recursive(N-1, 0, 1, map, visited, N, M, K);
    return 0;
}
