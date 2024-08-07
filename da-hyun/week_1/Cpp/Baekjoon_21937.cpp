#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;
int recursive(int index, bool visited[], vector<int> list[]){
    if(visited[index]) return 0;
    visited[index] = true;
    if(list[index].empty())return 1;
    int tmpAnswer = 1;
    for(auto i:list[index]){
        tmpAnswer += recursive(i, visited, list);
    }
    return tmpAnswer;
}

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, M;
    cin >> N >> M;
    vector<int> list[N+1];
    bool visited[N+1];
    memset(visited, 0, sizeof(visited));
    for(int i=0;i<M;i++){
        int A, B;
        cin >> A >> B;
        list[B].push_back(A);
    }
    int X;
    cin >> X;
    cout << recursive(X, visited, list)-1;
    return 0;
}
