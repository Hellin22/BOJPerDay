class Solution {
    public int[] solution(long n) {
        String str = n + "";
        int[] arr = new int[str.length()];
        for(int i = str.length()-1; i >=0; i--){
            arr[str.length()-1 -i] = str.charAt(i)-'0';
        }

        return arr;
        
        
    }
}