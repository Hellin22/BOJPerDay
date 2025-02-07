#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
constexpr auto unvisited = 0;
constexpr auto visited = 1;

using namespace std;

const int MAX = 150;
int graph[MAX][MAX];
bool isvisited[MAX][MAX];
int N;
vector<pair<int, int>> safearea(MAX, make_pair(0, 0));
int x_dir[4] = { 0, 0, -1, 1 };
int y_dir[4] = { 1, -1, 0, 0 };
int cnt = 0;

bool compare(pair<int, int> a, pair<int, int> b) {

	return a.first > b.first;
}

void dfs(int x, int y, int waterfall) {
	int xc; int yc;
	for (int i = 0; i < 4; i++) {
		xc = x + x_dir[i];
		yc = y + y_dir[i];
		if (isvisited[xc][yc] == unvisited && graph[xc][yc] > waterfall) {
			isvisited[xc][yc] = visited;
			dfs(xc, yc, waterfall);
		}
	}
}

int main() {
	cin >> N;
	memset(graph, 0, sizeof(graph));
	memset(isvisited, unvisited, sizeof(isvisited));

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> graph[i][j];
		}
	}

	// i는 장마철 물이 온 양이다. 즉, i보다 큰곳은 접근 가능하다는 것이다.
	for (int i = 0; i <= 100; i++) {
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++) {
				if (isvisited[j][k] == unvisited && graph[j][k] > i) {
					isvisited[j][k] = visited;
					cnt++; // 연결요소 증가
					dfs(j, k, i);
				}
			}
		}
		safearea[i] = make_pair(cnt, i); // 연결요소의 개수, 비의 수위
		memset(isvisited, unvisited, sizeof(isvisited));
		cnt = 0;
	}

	sort(safearea.begin(), safearea.end(), compare);
	cout << safearea[0].first << endl;
}