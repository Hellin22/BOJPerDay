#include <string>
#include <vector>
#include <iostream>
#include <unordered_set>
#include <algorithm>

using namespace std;

bool compare(string &a, string& b) {
    if(a.size() != b.size()){
        return a.size() > b.size();
    }
    else return a < b;
}

bool solution(vector<string> phone_book) {
    sort(phone_book.begin(), phone_book.end(), compare);

    unordered_set<string> st; // 해시 -> 순서 x -> 자료 탐색에 O(1)
    for (int i = 0; i < phone_book.size(); i++) {
        string s = phone_book[i];
        if (st.find(s) != st.end()) return false;

        string ss = "";
        for (int j = 0; j < s.size(); j++) {
            ss += s[j];
            st.insert(ss);
        }
    }
    return true;
}

// phone_book은 1~1,000,000개
// 각 번호의 길이는 1~20자리
// phone_book은 string 벡터
// 어떤 전화번호가 다른 전화번호의 접두어인지 확인해야함.
// -> 길이가 짧은 전화번호가 긴 번호의 접두어가 됨. (길이가 긴 번호는 짧은 번호의 접두어가 될 수 없음.)
// 0. phone_book을 길이가 다르면 길이가 긴것이 뒤에오게, 같다면 사전순으로 정렬하기
// 1. phone_book에서 하나 꺼내야함.
// 그 폰번호가 앞에서 본 폰의 접두어인지 확인 -> dp[전번]이 존재하는지 확인
// -> 순서가 필요없는 unordered_map 사용하기. 등록, 조회가 O(1) time.
// 2. 만약 없다? 그러면 1~s의 길이만큼 전번을 dp에 등록하기
// 3. 만약에 존재했다? 그러면 false
// 4. 만약에 phone_book 모두 돌았는데 없으면 true 리턴

