import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


class Main {
    public static void main(String[] args) throws IOException {
        int[][] arr = new int[41][2]; // 0~40 2열씩
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        arr[0][0] = 1;
        arr[0][1] = 0;
        arr[1][0] = 0;
        arr[1][1] = 1;

        for(int i = 2; i < arr.length; i++){
            for(int j = 0; j < arr[i].length; j++){
                arr[i][j] = arr[i-1][j] + arr[i-2][j];
            }
        }

        int t = Integer.parseInt(br.readLine());
        while(t-->0){
            int n = Integer.parseInt(br.readLine());
            sb.append(arr[n][0] + " " + arr[n][1] + "\n");
        }
        System.out.println(sb);
    }
}