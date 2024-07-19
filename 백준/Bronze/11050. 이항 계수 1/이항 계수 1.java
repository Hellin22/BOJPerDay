import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        k = Math.min(k, n-k);
        int summ = 1;
        for(int i = 0; i < k; i++) {
            summ *= n;
            n--;
        }
        for (int i = 1; i <= k; i++) {
            summ /= i;
        }
        System.out.println(summ);
    }
}