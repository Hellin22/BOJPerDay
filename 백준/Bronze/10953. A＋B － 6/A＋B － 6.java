import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String[] strs = br.readLine().split(",");
            int a = Integer.parseInt(strs[0]);
            int b = Integer.parseInt(strs[1]);
            sb.append(a+b).append("\n");
        }
        System.out.println(sb);
    }
}
