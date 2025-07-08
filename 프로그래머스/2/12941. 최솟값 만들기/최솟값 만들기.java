import java.util.*;
class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        List<Integer> arr1 = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();
        for(int i = 0; i < A.length; i++){
            arr1.add(A[i]);
            arr2.add(B[i]);
        }
        Collections.sort(arr1);
        Collections.sort(arr2, Collections.reverseOrder());//

        for(int i = 0; i < arr1.size(); i++){
            answer += arr1.get(i) * arr2.get(i);
        }
        return answer;
    }
}