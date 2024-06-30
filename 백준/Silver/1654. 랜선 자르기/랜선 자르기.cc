#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {

    cin.tie(NULL);
    long long K, N;
    vector<long long> line;

    cin >> K >> N;
    
    long long len;
    for (int i = 0; i < K; i++) {
        cin >> len;
        line.push_back(len);
    }
    sort(line.begin(), line.end());

    //이분탐색
    long long low = 1, high = line.at(K - 1), mid;
    long long ans = 0;
    while (low <= high) {
        mid = (low + high) / 2;
        int cnt = 0;       //cnt는 길이 mid인 랜선의 개수
        for (int i = 0; i < K; i++) {
            cnt += (int)(line[i] / mid);
        }

        //update
        if (cnt >= N) {
            low = mid + 1;
            if (ans < mid) ans = mid;
        }
        else high = mid-1;
    }
    cout << ans;
}