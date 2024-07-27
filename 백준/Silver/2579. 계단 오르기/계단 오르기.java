import java.io.*;
import java.util.Arrays;
import java.util.*;
public class Main {

    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = 0;

        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[2][n+1];
        int[] gyedan = new int [n+1];
        for(int i = 1; i <= n; i++) {
            int inputInt = Integer.parseInt(br.readLine());
            gyedan[i] = inputInt;
        }

        arr[0][1] = gyedan[1];
        arr[1][1] = 0;
        if(n == 1) {
            sum = gyedan[1];
        }
        else{
            for(int i = 2; i <= n; i++) {
                arr[0][i] = Math.max(arr[0][i-2], arr[1][i-2]) + gyedan[i];
                arr[1][i] = arr[0][i-1] + gyedan[i];
            }
            sum = Math.max(arr[0][n], arr[1][n]);
        }
        System.out.println(sum);


    }
}