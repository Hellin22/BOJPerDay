import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[][] arr = new int[100001][3];
    static int[][] max_min = new int[100001][3];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int max = -1; int min = 10;
        for (int i = 1; i <= n; i++) {
            String[] strs = br.readLine().split(" ");
            arr[i][0] = Integer.parseInt(strs[0]);
            arr[i][1] = Integer.parseInt(strs[1]);
            arr[i][2] = Integer.parseInt(strs[2]);
        }

        for(int i = 1; i <= n; i++){
            max_min[i][0] = Math.max(max_min[i-1][0], max_min[i-1][1]) + arr[i][0];
            max_min[i][1] = Math.max(max_min[i-1][0], Math.max(max_min[i-1][1], max_min[i-1][2])) + arr[i][1];
            max_min[i][2] = Math.max(max_min[i-1][1], max_min[i-1][2]) + arr[i][2];
        }
        max = Math.max(max_min[n][0], Math.max(max_min[n][1], max_min[n][2]));
        for(int i = 1; i <= n; i++){
            max_min[i][0] = 0;
            max_min[i][1] = 0;
            max_min[i][2] = 0;
        }
        for(int i = 1; i <= n; i++){
            max_min[i][0] = Math.min(max_min[i-1][0], max_min[i-1][1]) + arr[i][0];
            max_min[i][1] = Math.min(max_min[i-1][0], Math.min(max_min[i-1][1], max_min[i-1][2])) + arr[i][1];
            max_min[i][2] = Math.min(max_min[i-1][1], max_min[i-1][2]) + arr[i][2];
        }
        min = Math.min(max_min[n][0], Math.min(max_min[n][1], max_min[n][2]));

        System.out.println(max + " " + min);
    }
}