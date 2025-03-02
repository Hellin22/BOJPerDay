#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
constexpr int unvisited = 0;
constexpr int visited = 1;
using namespace std;


// 입력 : M, N, K 
// K개의 줄에 대해 직사각형의 왼쪽아래, 오른쪽위 꼭지점의 좌표가 주어진다.
// 1 <= M, N, K <= 100

// 출력 : 직사각형 영역에 포함되지 않은 영역의 개수 + 각 영역의 오름차순 출력

const int MAX = 120;

int M, N, K;
int graph[MAX][MAX];
bool isvisited[MAX][MAX];
int x_dir[4] = { 0, 0, 1, -1 };
int y_dir[4] = { 1, -1, 0, 0 };
int cnt = 0;
int areacnt = 0;

void dfs(int x, int y) {
	int xc, yc;
	for (int i = 0; i < 4; i++) {
		xc = x + x_dir[i];
		yc = y + y_dir[i];
		if (xc < 0 || yc < 0 || xc >= M || yc >= N || isvisited[xc][yc] == visited) continue;

		graph[xc][yc] = cnt;
		areacnt++;
		isvisited[xc][yc] = visited;
		dfs(xc, yc);
	}
}


int main() {
	memset(graph, 0, sizeof(graph));
	memset(isvisited, unvisited, sizeof(isvisited));

	cin >> M >> N >> K; // M = 5, N = 7이면 (0, 7)도 가능해진다. 따라서 M N 순서로 반복
	int x1, y1;
	int x2, y2;
	for (int i = 0; i < K; i++) {
		cin >> x1 >> y1 >> x2 >> y2; // 왼쪽아래, 오른쪽 위 좌표이므로 x1y1이 무조건 더 작다.
		for (int j = x1; j <= x2-1; j++) {
			for (int k = y1; k <= y2-1; k++) {
				isvisited[k][j] = visited;
			}
		}
	}
	vector<int> areavector;

	//for (int i = 0; i < M; i++) {
	//	for (int j = 0; j < N; j++) {
	//		cout << isvisited[i][j] << " ";
	//	}
	//	cout << endl;
	//}

	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			if (isvisited[i][j] == visited) continue;
			areacnt = 1;
			isvisited[i][j] = visited;
			cnt++;
			graph[i][j] = cnt;
			dfs(i, j);
			areavector.push_back(areacnt);
		}
	}

	cout << cnt << endl;
	sort(areavector.begin(), areavector.end());
	for (auto i : areavector) {
		cout << i << " ";
	}

	//for (int i = 0; i <= M; i++) {
	//	/*for (int j = N; j >= 0; j--) */
	//	for(int j = 0; j <= N; j++){
	//		cout << graph[i][j] << " ";
	//	}
	//	cout << endl;
	//}

	//cout << endl;
}

// 22분 40초
 //49.49.49 방법을 바꿔야 겠다.


