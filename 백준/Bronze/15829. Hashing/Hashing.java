import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main{
    public static void main(String[] args) throws IOException {
        StringBuilder stringbuilder = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int L = Integer.parseInt(br.readLine());
        String str = br.readLine();

        // 소수인 r의 제곱수 값들을 저장해놔야함. -> dp 0~49값 저장해놓기
        long[] arr = new long[50];
        arr[0] = 1;
        for(int i = 1; i < 50; i++){
            arr[i] = (arr[i-1] * 31) % 1234567891;
        }
        long summ = 0;
        for(int i = 0; i < str.length(); i++){
            char c = str.charAt(i);
            int cInt = (int) c - 'a' + 1;
            summ = (summ + (cInt * arr[i])) % 1234567891;
        }
        System.out.println(summ);
    }
}