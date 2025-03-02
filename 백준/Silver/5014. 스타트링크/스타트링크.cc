#include <iostream>
#include <queue>
#include <algorithm>
#include <cstring>

constexpr int unvisited = 0;
constexpr int visited = 1;
using namespace std;

// F, S, G, U, D
// S는 현재위치 G는 도착위치 F는 꼭대기  1 ~ 백만
// U, D는 각각 몇칸 up, down 의미  0 ~ 백만

// 최솟값을 찾는 문제이므로 bfs를 사용한다. 또한 y축만 존재하기 때문에 백만의 bool 배열을 선언해도 메모리 초과가 발생하지 않는다.
// 엘레베이터로 이동할 수 없을 때를 어떻게 구할까?
// 만약 q가 빈다면 없는것이므로 cout 해주기.. 근데 시간이 너무 오래걸릴거 같다. 
// > 최대 백만이기 때문에 시간초과 x일거 같다.

const int MAX = 2000000;
bool isvisited[MAX];


int main() {
	memset(isvisited, unvisited, sizeof(isvisited));

	int F, S, G, U, D;
	cin >> F >> S >> G >> U >> D;

	if (S == G) {
		cout << 0 << endl; return 0;
	}
	else if (S > G && D == 0) {
		cout << "use the stairs" << endl; return 0;
	}
	else if (S < G && U == 0) {
		cout << "use the stairs" << endl; return 0;
	}

	queue<pair<int, int>> q;
	int y_dir[2] = { U, -D }; 
	// 헷갈렸던게 U, D로 넣으면 이전에 선언한 변수가 들어가는지 아스키코드가 들어가는지 헷갈렸는데 변수가 들어간다.
	// -D로 해도 상관없는거같다.
	q.push(make_pair(S, 0));
	isvisited[S] = visited;
	isvisited[0] = visited;

	int y, yc, cnt;

	while (!q.empty()) {
		y = q.front().first;
		cnt = q.front().second;

		//cout << y << " " << cnt << " " << endl;
		for (int i = 0; i < 2; i++) {
			yc = y + y_dir[i];
			
			if (yc > F || yc < 0 || isvisited[yc] == visited) continue;
			//cout << y << " " << cnt << " " << yc << " " << endl;
			if (yc == G) {
				cout << cnt + 1 << endl;
				return 0;
			}
			q.push(make_pair(yc, cnt+1));
			isvisited[yc] = visited;

		}

		q.pop();
		
	}

	cout << "use the stairs" << endl;
}

// 1 10 2 1
// 3 5 7 9 8 10
// 3 5 4 6 8 10