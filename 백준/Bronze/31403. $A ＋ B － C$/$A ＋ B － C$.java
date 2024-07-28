import java.io.*;
import java.util.Arrays;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine());

        String str = a + "" + b;
        System.out.println(a + b - c);
        System.out.println(Integer.parseInt(str) - c);
    }
}