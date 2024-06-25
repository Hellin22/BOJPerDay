#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int dp[501][501];

int solution(vector<vector<int>> triangle) {
	memset(dp, 0, sizeof(dp));
	// 입력 = triangle
	// 높이는 1~500이고 숫자는 0~9,999이하의 정수
	// result를 int가 담을 수 있냐를 계산
	// -> 501 * 205 * 9999 -> 12억~ ... 
	// 위 수보다 현저히 작은 수가 result 이므로 int 사용하기

	// int dp[501][501] 사용. 
	// dp[i][j] = i-1 높이의 j에 도달했을 때 숫자 합의 최대치
	// j는 0부터 i까지 증가하며 i에 다다르면 i는 1 증가
	// 점화식과 초기값
	// 초기값 dp[0][0] = triangle[0][0]
	// dp[1][0] = triangle[1][0] + dp[0][0]
	// dp[1][1] = triangle[1][1] + dp[0][0]

	dp[0][0] = triangle[0][0];
	dp[1][0] = triangle[1][0] + dp[0][0];
	dp[1][1] = triangle[1][1] + dp[0][0];

	for (int i = 2; i < triangle.size(); i++) {
		// 제일 왼쪽
		dp[i][0] = dp[i - 1][0] + triangle[i][0];
		for (int j = 1; j <= i-1; j++) {
			dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j];
		}
		// 제일 오른쪽
		dp[i][i] = dp[i - 1][i - 1] + triangle[i][i];
	}

	int maxx = 0;
	for (int i = 0; i < triangle.size(); i++) {
		maxx = max(maxx, dp[triangle.size()-1][i]);
	}
    
	return maxx;
}