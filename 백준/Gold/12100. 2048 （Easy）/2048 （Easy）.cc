// 66분
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int n;
int arr[21][21];
int maxx = -1;
int isvisited[21][21];

void up() {
	// 모든 col에 대해서 진행.
	memset(isvisited, 0, sizeof(isvisited));

	for (int j = 0; j < n; j++) {
		for (int i = 1; i < n; i++) {
			if (arr[i][j] == 0) continue;
			int k = i-1;
			while (1) {
				if (k == 0 && arr[k][j] == 0) {
					arr[k][j] = arr[i][j];
					arr[i][j] = 0;
					break;
				}
				else if (k != 0 && arr[k][j] == 0) {
					k--;
				}
				else if (arr[k][j] != 0) {
					if (arr[k][j] != arr[i][j]) {
						if (k + 1 == i) break; // 위치 그대로인 경우
						else {
							arr[k + 1][j] = arr[i][j];
							arr[i][j] = 0;
							break;
						}
					}
					else if (arr[k][j] == arr[i][j]) {
						if (isvisited[k][j] == 0) {
							arr[k][j] = arr[k][j] * 2;
							arr[i][j] = 0;
							isvisited[k][j] = 1;
							break;
						}
						else if (isvisited[k][j] = 1) {
							if (k + 1 == i) break;
							else {
								arr[k + 1][j] = arr[i][j];
								arr[i][j] = 0;
								break;
							}
						}
					}
				}
			}
		}
	}
}

void down() { // 아래로 내려야한다.
	memset(isvisited, 0, sizeof(isvisited));
	for (int j = 0; j < n; j++) {
		for (int i = n-2; i >= 0; i--) {
			if (arr[i][j] == 0) continue;

			int k = i + 1; 
			while (1) {
				if (k == n-1 && arr[k][j] == 0) {
					arr[k][j] = arr[i][j];
					arr[i][j] = 0;
					break;
				}
				else if (k != 0 && arr[k][j] == 0) {
					k++;
				}
				else if (arr[k][j] != 0) {
					if (arr[k][j] != arr[i][j]) {
						if (k - 1 == i) break;
						else {
							arr[k - 1][j] = arr[i][j];
							arr[i][j] = 0;
							break;
						}
					}
					else if (arr[k][j] == arr[i][j]) {
						if (isvisited[k][j] == 0) {
							arr[k][j] = arr[k][j] * 2;
							arr[i][j] = 0;
							isvisited[k][j] = 1;
							break;
						}
						else if (isvisited[k][j] = 1) {
							if (k - 1 == i) break;
							else {
								arr[k - 1][j] = arr[i][j];
								arr[i][j] = 0;
								break;
							}
						}
					}
				}
			}
		}
	}
}

void left() {
	memset(isvisited, 0, sizeof(isvisited));

	for (int i = 0; i < n; i++) {
		for (int j = 1; j < n; j++) {
			if (arr[i][j] == 0) continue;
			int k = j - 1; 
			while (1) {
				if (k == 0 && arr[i][k] == 0) {
					arr[i][k] = arr[i][j];
					arr[i][j] = 0;
					break;
				}
				else if (k != 0 && arr[i][k] == 0) {
					k--;
				}
				else if (arr[i][k] != 0) {
					if (arr[i][k] != arr[i][j]) {
						if (k + 1 == j) break;
						else {
							arr[i][k + 1] = arr[i][j];
							arr[i][j] = 0;
							break;
						}
					}
					else if (arr[i][k] == arr[i][j]) {
						if (isvisited[i][k] == 0) {
							arr[i][k] = arr[i][k] * 2;
							arr[i][j] = 0;
							isvisited[i][k] = 1;
							break;
						}
						else if (isvisited[i][k] == 1) {
							if (k + 1 == j) break;
							else {
								arr[i][k + 1] = arr[i][j];
								arr[i][j] = 0;
								break;
							}
						}
					}
				}
			}
		}
	}
}

void right() {
	memset(isvisited, 0, sizeof(isvisited));

	for (int i = 0; i < n; i++) {
		for (int j = n-2; j >= 0; j--) {
			if (arr[i][j] == 0) continue;

			int k = j + 1; 
			while (1) {
				if (k == n-1 && arr[i][k] == 0) {
					arr[i][k] = arr[i][j];
					arr[i][j] = 0;
					break;
				}
				else if (k != 0 && arr[i][k] == 0) {
					k++;
				}
				else if (arr[i][k] != 0) {
					if (arr[i][k] != arr[i][j]) {
						if (k - 1 == j) break;
						else {
							arr[i][k - 1] = arr[i][j];
							arr[i][j] = 0;
							break;
						}
					}
					else if (arr[i][k] == arr[i][j]) {
						if (isvisited[i][k] == 0) {
							arr[i][k] = arr[i][k] * 2;
							arr[i][j] = 0;
							isvisited[i][k] = 1;
							break;
						}
						else if (isvisited[i][k] == 1) {
							if (k - 1 == j) break;
							else {
								arr[i][k - 1] = arr[i][j];
								arr[i][j] = 0;
								break;
							}
						}
					}
				}
			}
		}
	}
}

void dfs(int cnt) {
	if (cnt == 6) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				maxx = max(maxx, arr[i][j]);
			}
		}
		return;
	}

	int tmparr[21][21];

	copy(&arr[0][0], &arr[0][0] + 21 * 21, &tmparr[0][0]);
	up();
	dfs(cnt + 1);
	copy(&tmparr[0][0], &tmparr[0][0] + 21 * 21, &arr[0][0]);

	copy(&arr[0][0], &arr[0][0] + 21 * 21, &tmparr[0][0]);
	down();
	dfs(cnt + 1);
	copy(&tmparr[0][0], &tmparr[0][0] + 21 * 21, &arr[0][0]);

	copy(&arr[0][0], &arr[0][0] + 21 * 21, &tmparr[0][0]);
	left();
	dfs(cnt + 1);
	copy(&tmparr[0][0], &tmparr[0][0] + 21 * 21, &arr[0][0]);

	copy(&arr[0][0], &arr[0][0] + 21 * 21, &tmparr[0][0]);
	right();
	dfs(cnt + 1);
	copy(&tmparr[0][0], &tmparr[0][0] + 21 * 21, &arr[0][0]);
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
		}
	}

	dfs(1);
	cout << maxx << '\n';
}