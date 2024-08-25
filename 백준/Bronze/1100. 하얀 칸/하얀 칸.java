import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

class Main {
    public static void main(String[] args) throws IOException {
        // 00 02 04 06
        // 11 13 15 17
        // 20 22 24 26
        // -> i%2 == 0이면 j도 %2인 부분만 확인

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strs = new String[8];
        int answer = 0;
        for(int i = 0; i < 8; i++){
            strs[i] = br.readLine();
        }
        for(int i = 0; i < strs.length; i++){
            if(i%2 == 0){
                for(int j = 0; j < strs[i].length(); j+=2){
                    if(strs[i].charAt(j) == '.') continue;
                    answer++;
                }
            }
            else{
                for(int j = 1; j < strs[i].length(); j+=2){
                    if(strs[i].charAt(j) == '.') continue;
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }
}
