#include <iostream>
#include <queue>
#include <vector>

using namespace std;

// 입력
// N(1~1000) 도시의 개수, M(1~100,000) 버스의 개수. 도시는 정점, 버스는 간선 의미
// 3번째 줄부터는 버스의 정보 (from, to, 가중치) (가중치 0~99,999)
// 마지막에는 from, to의 정보가 주어지고 무조건 갈 수 있다.
// 출력
// 마지막줄의 from에서 to로 가는 최소비용 출력
// -> 다익스트라 사용
// + 한 도시에서 출발하여 다른 도시에 도착하는 버스들 = directed

const int INF = 987654321;

//int graphdist[1001][1001];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N, M;
	cin >> N >> M;
	vector<vector<pair<int, int>>> graph(N + 1); // 도시는 1번부터 존재하므로 1~N 사용
	int from, to, dist;

	//for (int i = 0; i < 1001; i++) {
	//	for (int j = 0; j < 1001; j++) {
	//		graphdist[i][j] = INF;
	//	}
	//}

	for (int i = 0; i < M; i++) {
		cin >> from >> to >> dist;
		// if (graphdist[from][to] < dist) continue;
		graph[from].push_back(make_pair(to, dist));
	}
	cin >> from >> to;

	vector<int> distance(N + 1);

	for (int i = 1; i <= N; i++) {
		distance[i] = INF;
	}

	priority_queue < pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push(make_pair(0, from));
	distance[from] = 0;

	while (!pq.empty()) {
		dist = pq.top().first;
		int v = pq.top().second;
		pq.pop();

		if (distance[v] < dist) continue;
		// 이미 v로 가는 최소비용이 갈 수 있는 비용보다 작은 경우 
        // 간선의 가중치를 더해도 최소가 되기는 불가하므로 continue

		for (int i = 0; i < graph[v].size(); i++) {
			int vv = graph[v][i].first;
			int dist2 = graph[v][i].second;

			if (distance[vv] > dist + dist2) {
				distance[vv] = dist + dist2;
				pq.push(make_pair(dist + dist2, vv));
			}
		}
	}
	cout << distance[to] << '\n';
}