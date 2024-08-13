import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            if(i % 10 == 0 && i != 0)sb.append("\n").append(s.charAt(i));
            else sb.append(s.charAt(i));
        }
        System.out.println(sb);
    }
}