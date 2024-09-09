#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>
#define FAST cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
using namespace std;

struct cmp {
	bool operator()(int a, int b) {
		if (abs(a) != abs(b)) {
			return abs(a) > abs(b);
		}
		else return a > b;
	}
};

int main() {
	FAST;
	int n;
	cin >> n;

	priority_queue<int, vector<int>, cmp> pq;
	//vector<int> v;
	while (n--) {
		int x;
		cin >> x;
		if (x == 0) {
			if (pq.empty()) {
				cout << 0 << '\n';
				//v.push_back(0);
			}
			else {
				cout << pq.top() << '\n';
				//v.push_back(pq.top());
				pq.pop();
			}
			continue;
		}

		pq.push(x);
	}
}