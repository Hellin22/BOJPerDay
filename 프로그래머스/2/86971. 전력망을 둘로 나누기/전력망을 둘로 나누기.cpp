#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <queue>
#include <iostream>

using namespace std;

int arr[101];

int solution(int n, vector<vector<int>> wires) {
    
    int answer = 101;
    vector<vector<int>> graph(n+1);
    for(int i = 0; i < wires.size(); i++){
        graph[wires[i][0]].push_back(wires[i][1]);
        graph[wires[i][1]].push_back(wires[i][0]);
    }
    
    for(int i = 0; i < wires.size(); i++){
        memset(arr, 0, sizeof(arr));
        int a = wires[i][0];
        int b = wires[i][1]; // a, b는 연결이 끊김.
        int fir = 0;
        int sec = 0; // 하나의 트리 형태 -> n - fir이 sec임.
        // 결국 fir - sec를 해야하는데 sec는 n-fir이니까 2fir의 최소가 답이된다.
        // 또는 sec - fir -> n-fir-fir
        // 따라서 n-2fir을 하고 음수면 -1 곱하기
        // node는 1~n까지 존재. 1번을 먼저 bfs
        queue<int> q;
        q.push(1);
        arr[1] = 1;
        fir++;
        while(!q.empty()){
            int num = q.front();
            q.pop();
            
            for(int j = 0; j < graph[num].size(); j++){
                // 1. a != num && b != graph[num][j]
                // 2. b != num && a != graph[num][j]
                // + arr[graph[num][j]] != 1
                if(a == num && b == graph[num][j]) continue;
                if(a == graph[num][j] && b == num) continue;
                if(arr[graph[num][j]] == 1) continue;
                
                q.push(graph[num][j]);       
                fir++;
                arr[graph[num][j]] = 1;
                /*if((a != num || b != graph[num][j]) 
                   && (b != num && a != graph[num][j])){
                    if(arr[graph[num][j]] != 1){
                        q.push(graph[num][j]);       
                        fir++;
                        arr[graph[num][j]] = 1;
                    }
                }*/
            }
        }
        int tmpans = n - fir*2;
        if(tmpans < 0) tmpans*=-1;
        answer = min(answer, tmpans);
    }
    
    return answer;
}