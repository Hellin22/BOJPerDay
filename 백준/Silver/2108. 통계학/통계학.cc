#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#define FAST cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
using namespace std;

int main() {
    int n;
    cin >> n; // n개는 홀수개

    int summ = 0; // 모든 수의 합 저장 공간 필요. -> long long 안써도 됨. (최대 20억)

    int mid_gabs = 0; // 숫자를 통째로 저장하는 공간 필요.
    vector<int> mid_gabs_vector;

    int most_gabs = 0; // 숫자의 개수를 저장할 공간 필요
    vector<pair<int, int>> arr;
    for (int i = 0; i <= 8000; i++) {
        arr.push_back({ 0, i }); // first는 빈도수, second는 실제 숫자+4000 한것.
    }

    int max_minus_min = 0; // max와 min을 저장할 공간 필요
    int maxx = -4001; int minn = 4001;


    for (int i = 0; i < n; i++) {
        int a;
        cin >> a; // a는 절대값이 4000 이하이다.
        summ += a; // 1번
        mid_gabs_vector.push_back(a); // 2번 -> 마지막에 sort

        arr[a + 4000].first--; // 3번

        maxx = max(maxx, a);
        minn = min(minn, a); // 4번
    }

    if (summ % n != 0) {
        if (summ > 0) {
            if (summ % n > n / 2) {
                // 반올림을 해야함.
                cout << summ / n + 1 << '\n';
            }
            else cout << summ / n << '\n';
        }
        else { // 음수
            if (-summ % n > n / 2) { // -9 / 5 -> -1.8
                cout << summ / n - 1 << '\n';
            }
            else cout << summ / n << '\n';
        }
    }
    else cout << summ / n << '\n'; // 1번

    sort(mid_gabs_vector.begin(), mid_gabs_vector.end());
    cout << mid_gabs_vector[n / 2] << '\n'; // 2번

    // 최빈값이 여러개면 2번째로 작은값 출력 -> 모든 값들을 다 봐야함.
    sort(arr.begin(), arr.end());
    int ccnt1 = arr[0].first;

    vector<int>thr;
    thr.push_back(arr[0].second);

    for (int i = 1; i < arr.size(); i++) {
        if (arr[i].first == ccnt1) thr.push_back(arr[i].second);
    }
    sort(arr.begin(), arr.end());

    int gabs1;
    if (thr.size() == 1) {
        gabs1 = thr[0]-4000;
    }
    else {
        gabs1 = thr[1]-4000;
    }
    cout << gabs1 << '\n'; // 3번

    cout << maxx - minn << '\n'; // 4번

}