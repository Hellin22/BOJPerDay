import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;
class Main{
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());
        while(t-->0){
            String[] strs = br.readLine().split(" ");
            int a = Integer.parseInt(strs[0]);
            for(int i = 0; i < strs[1].length(); i++){
                for(int j = 0; j < a; j++){
                    sb.append(strs[1].charAt(i));
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}