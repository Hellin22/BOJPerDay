#include <iostream>
#include <cstring>
using namespace std;

int arr[1000010];

int main() {
	cin.tie(0);
	cout.tie(0);
	ios_base::sync_with_stdio(0);

	memset(arr, 0, sizeof(arr));
	int m, n; // m이상 n이하 소수 출력
	cin >> m >> n; // 1000000이하
	arr[1] = -1;
	
	// 합성수면 -1로 바꾸기
	for (int i = 2; i * i <= n; i++) {
		
		if (arr[i] == -1) continue;
		
		for (int j = i * i; j <= n; j += i) {
			arr[j] = -1;
		}
	}

	for (int i = m; i <= n; i++) {
		if (arr[i] == 0) cout << i << '\n';
	}

}