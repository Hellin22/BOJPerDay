import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        HashMap<Integer, Integer> map = new HashMap<>();
        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {

            int x = Integer.parseInt(st.nextToken());
            if(map.containsKey(x)) {
                map.put(x, map.get(x) + 1);
            }else{
                map.put(x, 1);
            }
        }
        StringBuilder stringBuilder = new StringBuilder();
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int x = Integer.parseInt(st.nextToken());
            if(map.containsKey(x)) {
                stringBuilder.append(map.get(x) + " ");
            }else {
                stringBuilder.append(0 + " ");
            }
        }
        System.out.print(stringBuilder);
    }
}
