#include <iostream>
#include <vector>
#include <cstring>
#define FAST cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
using namespace std;

int arr[1001];

int main() {
	FAST;
	memset(arr, 0, sizeof(arr)); // 0인 경우에는 소수임.
	int n;
	cin >> n;
	vector<int> v(n);
	for (int i = 0; i < n; i++) cin >> v[i];

	arr[1] = 1;
	for (int i = 2; i * i <= 1000; i++) {
		if (arr[i] == 1) continue;
		for (int j = i * i; j <= 1000; j += i) arr[j] = 1;
	}

	int cnt = 0;
	for (int i = 0; i < n; i++) if (arr[v[i]] == 0) cnt++;
	cout << cnt;
}