import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int answer = 0;
        int fiveMogs = n/5;
        for(int i = 0; i < 3; i++) {
            // 5의 개수를 하나씩 빼면서 확인.
            if((n - fiveMogs*5)% 3 == 0){
                answer = fiveMogs + (n - fiveMogs*5)/3;
                break;
            }
            fiveMogs-=1;
            if(fiveMogs== -1) break;
        }
        if(answer == 0) System.out.println(-1);
        else System.out.println(answer);
    }
}
