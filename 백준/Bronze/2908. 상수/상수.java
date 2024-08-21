import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strs = br.readLine().split(" ");
        String[] strs2 = new String[2];

        for(int i = 0; i < 2; i++){
            String toReverse = strs[i];
            String str = "";
            for(int j = 0; j < 3; j++){
                // 세자리수
                str+=toReverse.charAt(2-j);
            }
            strs2[i] = str;
        }

        System.out.println(Math.max(Integer.parseInt(strs2[0]), Integer.parseInt(strs2[1])));
    }
}