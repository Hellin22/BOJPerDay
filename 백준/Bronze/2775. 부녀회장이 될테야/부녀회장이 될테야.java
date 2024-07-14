import java.util.*;

public class Main {
    public static void main(String[] args) {

        long[][] arr = new long[15][15];

        for (int i = 1; i <= 14; i++) {
            arr[0][i] = i;
        }

        for (int i = 1; i <= 14; i++) {
            for (int j = 1; j <= 14; j++) {
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1];
            }
        }
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t != 0) {
            int k = sc.nextInt();
            int n = sc.nextInt();
            t--;
            System.out.println(arr[k][n]);
        }

    }
}


// 0층 부터 k층까지 존재. -> 14층까지 존재 행은 15로 선언
// 호수는 1호부터 존재. -> 1~14호 -> 열도 15로 선언

// 0층 1 2 3 4 5 6 ... 14
// 1층 1 3