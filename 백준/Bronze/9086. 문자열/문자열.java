import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++) {
            String s = br.readLine();
            if(s.length() == 1){
                sb.append(s.charAt(0)).append(s.charAt(0)).append("\n");
            }else{
                sb.append(s.charAt(0)).append(s.charAt(s.length()-1)).append("\n");
            }
        }
        System.out.println(sb);
    }
}
