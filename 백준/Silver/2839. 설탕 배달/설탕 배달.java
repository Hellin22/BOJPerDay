import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] dp = new int[N + 1];
        if(N >= 3) dp[3] = 1;
        if(N >= 5) dp[5] = 1;
        for (int i = 6; i <= N; i++) {
            if(dp[i-3] == 0 || dp[i-5] == 0) dp[i] = Math.max(dp[i-3], dp[i-5]) + 1;
            else dp[i] = Math.min(dp[i-3], dp[i-5]) + 1;
            if(dp[i] == 1) dp[i] = 0;
        }
        if(dp[N] == 0) {
            System.out.println(-1);
            return;
        }
        System.out.println(dp[N]);
    }
}
