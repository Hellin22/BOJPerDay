#include <iostream>
#include <vector>
#include <queue>
#define FAST cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);

using namespace std;

int main() {
	FAST;
	int t;
	cin >> t;
	while (t--) {
		vector<int> pri_cnt(10, 0);
		vector<int> sunser(1, 0);
		int maxx = -1;
		queue<pair<int, int>> q; // 중요도, 순번

		int humanCnt, wantCnt;
		cin >> humanCnt >> wantCnt;
		int pri;
		for (int i = 0; i < humanCnt; i++) {
			cin >> pri;
			pri_cnt[pri]++;
			q.push({ pri, i });
			maxx = max(maxx, pri);
		}

		while (!q.empty()) {
			if (pri_cnt[maxx] == 0) {
				for (int i = maxx - 1; i > 0; i--) {
					if (pri_cnt[i] != 0) {
						maxx = i;
						break;
					}
				}
			} // maxx를 찾음.
			int cur_pri = q.front().first;
			int cur_sunser = q.front().second;
			q.pop();

			if (maxx == cur_pri) {
				pri_cnt[cur_pri]--;
				if (cur_sunser == wantCnt) {
					cout << sunser.size() << '\n';
					break ;
				}
				else sunser.push_back(cur_sunser + 1);
			}
			else q.push({ cur_pri, cur_sunser }); // 다시 뒤에 넣기
		}
	}
}