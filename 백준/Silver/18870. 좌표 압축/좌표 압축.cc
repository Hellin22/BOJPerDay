#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

struct cmp {
    bool operator()(pair<int, int> a, pair<int, int> b) {
        return a.first > b.first;
    }
};


int main() {
    priority_queue <pair<int, int>, vector<pair<int, int>>, cmp> pq;

    int n;
    cin >> n;
    vector<int> v(n + 1, 0); // v[i]에 변환한 좌표 저장
    for (int i = 1; i <= n; i++) {
        cin >> v[i];
        pq.push({ v[i] , i }); // pq에는 실제 값과 idx 정보 저장
        // pq는 실제값 기반으로 오름차순 저장
    }

    int rank = 0;
    int x = pq.top().first;
    int idx = pq.top().second;
    v[idx] = rank;
    int preNum = x;

    pq.pop();

    while (!pq.empty()) {
        x = pq.top().first;
        idx = pq.top().second;
        pq.pop();

        if (preNum == x) {
            v[idx] = rank;
        }
        else {
            rank++;
            v[idx] = rank;
        }
        preNum = x;
    }
    for (int i = 1; i <= n; i++) {
        cout << v[i] << " ";
    }
}