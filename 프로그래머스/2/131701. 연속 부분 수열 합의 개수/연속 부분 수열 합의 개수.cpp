#include <string>
#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;

int solution(vector<int> elements) {
    // 중복 없어야함, 개수만 필요 -> unordered_set 사용
    // 결국 원형 배열이랑 같음.
    // elements.size()를 %하면 된다.
    // size가 5일 때 0 1 2 3 4 (5%5) (6%5) ...
    int answer = 0;
    unordered_set<int> st;
    // 1개 ~ 5개(size) 만큼 반복해야함. 
    // -> 해당 개수만큼의 합 (ex. 1개 합개수 + 2개합 개수 + ... ) 
    // size만 1개 나오고 나머지는 모두 size개가 나온다.
    int sum = 0;
    for(int i = 1; i < elements.size(); i++){ 
        for(int start_idx = 0; start_idx < elements.size(); start_idx++){
            sum = 0;
            for(int plus_idx = 0; plus_idx < i; plus_idx++){
                sum+=elements[(start_idx + plus_idx) % elements.size()];
            }
            st.insert(sum);
        }
        
    }
    // 내가 하고싶은건 원소가 1개일때, 2개일때 ... n개일때 반복
    // 1개일때 시작 idx부터 0, 1, 2, 3, 4 or 0,1 1,2 ... 4,0 
    // 시작 idx를 하는게 아니라 
    
    
    // size 크기 일때는 따로 처리
    sum = 0;
    for(int i = 0; i < elements.size(); i++){
        sum+= elements[i];
    }
    st.insert(sum);
    return st.size();
}