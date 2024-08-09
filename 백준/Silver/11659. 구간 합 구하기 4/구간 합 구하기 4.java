import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String[] strs = br.readLine().split(" ");
        int n = Integer.parseInt(strs[0]);
        int m = Integer.parseInt(strs[1]);

        ArrayList<Integer> arr = new ArrayList<>();
        ArrayList<Integer> sum = new ArrayList<>();
        arr.add(0);
        sum.add(0);

        strs = br.readLine().split(" ");
        for(int i = 0; i < strs.length; i++){
            arr.add(Integer.parseInt(strs[i]));
            sum.add(Integer.parseInt(strs[i]) + sum.get(i));
        }
        
        for(int i = 0; i < m; i++){
            strs = br.readLine().split(" ");
            int a = Integer.parseInt(strs[0]);
            int b = Integer.parseInt(strs[1]);

            sb.append(sum.get(b) - sum.get(a-1)).append("\n");
        }
        System.out.println(sb);
    }
}

