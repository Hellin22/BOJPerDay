import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> arr = new ArrayList<>();

        String[] strs = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr.add(Integer.parseInt(strs[i]));
        }
        int wantNum = Integer.parseInt(br.readLine());
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if(arr.get(i) == wantNum) ans++;
        }
        System.out.println(ans);
    }
}