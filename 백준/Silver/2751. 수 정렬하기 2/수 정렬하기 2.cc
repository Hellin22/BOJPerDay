#include <iostream>
#include <queue>
#include <vector>
#define FAST cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
using namespace std;

int main() {
    FAST;
    priority_queue<int,vector<int>, greater<int>> pq;
    int n;
    cin >> n;
    while (n--) {
        int inputInt;
        cin >> inputInt;
        pq.push(inputInt);
    }

    while (!pq.empty()) {
        cout << pq.top() << '\n';
        pq.pop();
    }
}