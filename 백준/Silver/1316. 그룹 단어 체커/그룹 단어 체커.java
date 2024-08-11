import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;
class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] alphabet = new int[26];
        int answer = 0;

        int n = Integer.parseInt(br.readLine());
        int tmpn = n;
        while(n-->0){
            Arrays.fill(alphabet, 0);
            String s = br.readLine();
            int before = s.charAt(0)-'a';
            alphabet[before]++;
            for(int i = 1; i < s.length(); i++) {
                // before와 현재가 같다면 ok -> 만약 다르다면 alphabet[현재]가 0이 아니라면 ++후 break;
                int cur = s.charAt(i)-'a';

                if(before == cur){
                    alphabet[cur]++;
                }else{
                    if(alphabet[cur] > 0){
                        answer++;
                        break;
                    } else {
                        alphabet[cur]++;
                        before = cur;
                    }
                }
            }
        }
        System.out.println(tmpn - answer);
    }
}