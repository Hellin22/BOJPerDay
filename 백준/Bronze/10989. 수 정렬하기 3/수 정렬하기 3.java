import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[10001]; // 1~10,000
        for(int i = 0; i < n; i++) {
            int nInput = Integer.parseInt(br.readLine());
            arr[nInput]++;
        }

        for(int i = 1; i <= 10000; i++) {
            for(int j = 0; j < arr[i]; j++) {
                sb.append(i).append("\n");
            }
        }
        System.out.println(sb);
    }
}