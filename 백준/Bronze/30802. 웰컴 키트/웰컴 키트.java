import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[6];
        int i = 0;
        while(st.hasMoreTokens()){
            arr[i] = Integer.parseInt(st.nextToken());
            i++;
        }
        st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        int tShirtMuggEm = 0;
        int penMuggEm = 0;
        int penOne = 0;
        for(int j = 0; j < 6; j++){
            tShirtMuggEm += (int)(Math.ceil((double)arr[j] / t));
        }
        penMuggEm = n / p;
        penOne = n % p;

        StringBuilder sb = new StringBuilder();
        sb.append(tShirtMuggEm).append("\n").append(penMuggEm).append(" ").append(penOne);

        System.out.println(sb);

    }
}