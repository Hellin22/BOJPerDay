
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;
import java.lang.StringBuilder;

class Main{
    public static void main(String[] args) throws IOException {
        // 교집합 찾는 문제
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        ArrayList<String> arr = new ArrayList<>();
        String[] strArr = br.readLine().split(" ");
        int n = Integer.parseInt(strArr[0]);
        int m = Integer.parseInt(strArr[1]);
        int cnt = 0;

        HashSet<String> hs = new HashSet<>();
        for(int i = 0; i < n; i++){
            hs.add(br.readLine());
        }
        for(int i = 0; i < m; i++){
            String input = br.readLine();
            if(hs.contains(input)){
                cnt++;
                arr.add(input);
            }
        }

        Collections.sort(arr);
        sb.append(arr.size() + "\n");
        for(int i = 0; i < arr.size(); i++){
            sb.append(arr.get(i) + "\n");
        }
        System.out.print(sb);
    }
}