#include <iostream>
#include <queue>
#define FAST cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);

using namespace std;

int main() {
	FAST;
	queue<int> q;

	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		q.push(i);
	}
	while (q.size() != 1) {
		q.pop();
		int froont = q.front();
		q.pop();
		q.push(froont);
	}
	int froont = q.front();
	cout << froont;
}