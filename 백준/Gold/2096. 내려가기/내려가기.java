import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
         int[][] arr = new int[n+1][3];
         int[][] maxx = new int[n+1][3];
         int[][] minn = new int[n+1][3];
        int max = -1; int min = 10;
        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
            arr[i][2] = Integer.parseInt(st.nextToken());
        }
        for(int i = 1; i <= n; i++){
            maxx[i][0] = Math.max(maxx[i-1][0], maxx[i-1][1]) + arr[i][0];
            maxx[i][1] = Math.max(maxx[i-1][0], Math.max(maxx[i-1][1], maxx[i-1][2])) + arr[i][1];
            maxx[i][2] = Math.max(maxx[i-1][1], maxx[i-1][2]) + arr[i][2];
            minn[i][0] = Math.min(minn[i-1][0], minn[i-1][1]) + arr[i][0];
            minn[i][1] = Math.min(minn[i-1][0], Math.min(minn[i-1][1], minn[i-1][2])) + arr[i][1];
            minn[i][2] = Math.min(minn[i-1][1], minn[i-1][2]) + arr[i][2];
        }
        max = Math.max(maxx[n][0], Math.max(maxx[n][1], maxx[n][2]));
        min = Math.min(minn[n][0], Math.min(minn[n][1], minn[n][2]));

        StringBuilder sb = new StringBuilder();
        System.out.println(sb.append(max).append(" ").append(min));
    }
}