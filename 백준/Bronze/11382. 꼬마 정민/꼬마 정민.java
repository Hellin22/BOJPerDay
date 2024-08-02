import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;
class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strs = br.readLine().split(" ");
        long a = Long.parseLong(strs[0]);
        long b = Long.parseLong(strs[1]);
        long c = Long.parseLong(strs[2]);

        System.out.println(a + b + c);
    }
}