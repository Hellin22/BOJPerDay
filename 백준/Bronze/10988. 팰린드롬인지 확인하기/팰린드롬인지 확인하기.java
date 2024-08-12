import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int answer = 1;
        for(int i = 0; i < s.length(); i++){
            if(i >= s.length()-i-1)break;
            if(s.charAt(i) != s.charAt(s.length()-i-1)){
                answer = 0;
                break;
            }
        }
        System.out.println(answer);
    }
}
