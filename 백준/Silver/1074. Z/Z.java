
import java.io.IOException;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static int cnt = 0;
    public static int r;
    public static int c;
    static boolean isFinish = false;

    public static void recursion(int n, int start1, int start2) {
        if (isFinish == true) return;
        if (n == 0) {
            if (start1 == r && start2 == c) {
                isFinish = true;
            }
            cnt++;
            return;
        }

        int njegob = 1;
        for (int i = 1; i <= n - 1; i++) {
            njegob *= 2;
        }

        if (r >= start1 && r <= start1 + njegob - 1 && c >= start2 && c <= start2 + njegob - 1) {
            recursion(n - 1, start1, start2);
            return;
        } else {
            cnt += (njegob * njegob);
        }

        if (r >= start1 && r <= start1 + njegob - 1 && c >= start2 + (njegob) && c <= start2 + (njegob) + njegob - 1) {
            recursion(n - 1, start1, start2 + njegob);
            return;
        }else{
            cnt += (njegob * njegob);
        }

        if (r >= start1 + (njegob) && r <= start1 + (njegob) + njegob - 1 && c >= start2 && c <= start2 + njegob - 1) {
            recursion(n - 1, start1 + njegob, start2);
            return;
        } else {
            cnt += (njegob * njegob);
        }

        if(r >= start1 + (njegob) && r <= start1 + (njegob) + njegob - 1 && c >= start2 + (njegob) && c <= start2 + (njegob) + njegob - 1){
            recursion(n - 1, start1 + njegob, start2 + njegob);
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        recursion(n, 0, 0);

        System.out.println(cnt - 1);
    }
}